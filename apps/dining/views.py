# zamar_springs/apps/dining/views.py
import hashlib
import re

from django.conf import settings
from django.core.cache import cache
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_GET

try:
    from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
except Exception:  # pragma: no cover - postgres features unavailable on sqlite
    SearchQuery = SearchRank = SearchVector = None

from .models import (
    DiningPage, FoodCategory, FoodItem,
    DiningSpace, FarmSource
)

SPACE_FALLBACK_IMAGE = "/static/images/web-pictures/open-air-dining-machakos.webp"
SEARCH_CACHE_TTL = 60 * 10
MENU_DATASET_CACHE_TTL = 60 * 15

SPACE_GALLERY_FALLBACKS = {
    "pergola": [
        "/static/images/web-pictures/pergola-outdoor-zamar-springs-gardens.webp",
        "/static/images/web-pictures/pergola-outdoor-zamar-springs-gardens-1.webp",
    ],
    "gazebo": [
        "/static/images/web-pictures/gazebo-setup-machakos.webp",
        "/static/images/web-pictures/gazebo-setup-machakos-2.webp",
    ],
    "open_air": [
        "/static/images/web-pictures/open-air-dining-machakos.webp",
        "/static/images/web-pictures/outdoor-dining-space-machakos-1.webp",
    ],
}


def _space_fallback_images(space):
    if space.space_type == "garden":
        return SPACE_GALLERY_FALLBACKS["open_air"]
    return SPACE_GALLERY_FALLBACKS.get(space.space_type, [])


def _decorate_space(space):
    if not space:
        return None

    gallery_images = list(space.gallery.all())
    space.gallery_images = gallery_images
    space.fallback_gallery = _space_fallback_images(space)

    if gallery_images:
        space.card_image = gallery_images[0].image.url
    elif space.fallback_gallery:
        space.card_image = space.fallback_gallery[0]
    else:
        space.card_image = SPACE_FALLBACK_IMAGE
    return space


def _normalize_query(query):
    return re.sub(r"\s+", " ", (query or "").strip().lower())


def _search_cache_key(query):
    hashed = hashlib.md5(query.encode("utf-8")).hexdigest()
    return f"dining:search:v1:{hashed}"


def _serialize_search_result(item, show_price=False):
    thumbnail = item["featured_image"] or ""
    if thumbnail and not str(thumbnail).startswith(("http://", "https://", "/")):
        thumbnail = f"{settings.MEDIA_URL}{thumbnail}"

    return {
        "id": item["id"],
        "name": item["name"],
        "slug": item["slug"],
        "category": item["category__name"],
        "category_slug": item["category__slug"],
        "thumbnail": thumbnail,
        "price": str(item["price"]) if show_price and item["price"] is not None else None,
        "url": f"{reverse('dining:menu')}#menu-list",
    }


def _build_cached_menu_dataset():
    key = "dining:search:dataset:v1"
    dataset = cache.get(key)
    if dataset is not None:
        return dataset

    qs = (
        FoodItem.objects.filter(is_active=True, category__is_active=True)
        .select_related("category")
        .values(
            "id",
            "name",
            "slug",
            "description",
            "search_tags",
            "farm_ingredients",
            "price",
            "featured_image",
            "category__name",
            "category__slug",
        )
        .order_by("category__display_order", "display_order")
    )
    dataset = []
    for row in qs:
        blob = " ".join(
            [
                row["name"] or "",
                row["description"] or "",
                row["search_tags"] or "",
                row["farm_ingredients"] or "",
                row["category__name"] or "",
            ]
        ).lower()
        row["search_blob"] = blob
        dataset.append(row)

    cache.set(key, dataset, MENU_DATASET_CACHE_TTL)
    return dataset


def _search_menu_items(query, limit=10):
    is_postgres = connection.vendor == "postgresql" and SearchVector is not None

    if is_postgres:
        search_vector = (
            SearchVector("name", weight="A")
            + SearchVector("description", weight="B")
            + SearchVector("search_tags", weight="A")
            + SearchVector("farm_ingredients", weight="C")
            + SearchVector("category__name", weight="B")
        )
        search_query = SearchQuery(query, search_type="websearch")
        qs = (
            FoodItem.objects.filter(is_active=True, category__is_active=True)
            .select_related("category")
            .annotate(search=search_vector, rank=SearchRank(search_vector, search_query))
            .filter(
                Q(search=search_query)
                | Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(search_tags__icontains=query)
                | Q(farm_ingredients__icontains=query)
                | Q(category__name__icontains=query)
            )
            .order_by("-rank", "category__display_order", "display_order")
            .values(
                "id",
                "name",
                "slug",
                "price",
                "featured_image",
                "category__name",
                "category__slug",
            )[:limit]
        )
        return list(qs)

    dataset = _build_cached_menu_dataset()
    filtered = [row for row in dataset if query in row["search_blob"]]
    return filtered[:limit]


@require_GET
def menu_search_api(request):
    query = _normalize_query(request.GET.get("q"))
    if len(query) < 2:
        response = JsonResponse({"results": []})
        response["X-Robots-Tag"] = "noindex, nofollow, noarchive"
        return response

    cache_key = _search_cache_key(query)
    cached = cache.get(cache_key)
    if cached is None:
        raw_results = _search_menu_items(query)
        cached = raw_results
        cache.set(cache_key, cached, SEARCH_CACHE_TTL)

    show_price_public = getattr(settings, "SHOW_MENU_PRICES_PUBLIC", True)
    show_price = bool(show_price_public or request.user.is_staff or request.user.is_superuser)
    results = [_serialize_search_result(item, show_price=show_price) for item in cached]

    response = JsonResponse({"results": results})
    response["Cache-Control"] = "private, max-age=60"
    response["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    return response


def dining_overview(request):
    """Dining landing page"""
    page_settings = DiningPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = DiningPage.objects.create()
    
    # Get active food categories with featured items
    categories = FoodCategory.objects.filter(
        is_active=True
    ).order_by('display_order')
    
    # Get featured food items (limit to show variety)
    featured_food = FoodItem.objects.filter(
        is_active=True,
        is_featured=True
    ).select_related('category').order_by('category__display_order', 'display_order')[:9]
    
    # Get dining spaces (for grouped expandable section)
    dining_spaces_qs = DiningSpace.objects.filter(
        is_active=True
    ).prefetch_related('gallery').order_by('display_order')
    dining_spaces = [_decorate_space(space) for space in dining_spaces_qs]
    pergola_space = _decorate_space(dining_spaces_qs.filter(space_type='pergola').first())
    gazebo_spaces = [_decorate_space(space) for space in dining_spaces_qs.filter(space_type='gazebo')]
    open_air_space = _decorate_space(dining_spaces_qs.filter(space_type='garden').first())
    
    # Get farm sources
    farm_sources = FarmSource.objects.filter(
        is_active=True
    ).order_by('display_order')
    
    context = {
        'page_settings': page_settings,
        'categories': categories,
        'featured_food': featured_food,
        'dining_spaces': dining_spaces,
        'pergola_space': pergola_space,
        'gazebo_spaces': gazebo_spaces,
        'open_air_space': open_air_space,
        'farm_sources': farm_sources,
    }
    return render(request, 'dining/overview.html', context)


def menu_view(request):
    """Menu page - PDF or food listing"""
    page_settings = DiningPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = DiningPage.objects.create()
    
    # Get all active food items grouped by category
    categories = FoodCategory.objects.filter(
        is_active=True
    ).order_by('display_order')
    
    # Get items for each category
    menu_data = []
    for category in categories:
        items = list(FoodItem.objects.filter(
            category=category,
            is_active=True
        ).order_by('display_order'))
        if items:
            menu_data.append({
                'category': category,
                'items': items
            })
    
    context = {
        'page_settings': page_settings,
        'menu_data': menu_data,
        'has_menu_pdf': bool(page_settings.menu_pdf),
    }
    return render(request, 'dining/menu.html', context)


def dining_spaces_view(request):
    """All dining spaces"""
    page_settings = DiningPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = DiningPage.objects.create()
    
    dining_spaces = DiningSpace.objects.filter(
        is_active=True
    ).order_by('display_order')
    
    # Group by type
    pergolas = dining_spaces.filter(space_type='pergola')
    gazebos = dining_spaces.filter(space_type='gazebo')
    garden_dining = dining_spaces.filter(space_type='garden')
    
    context = {
        'page_settings': page_settings,
        'pergolas': pergolas,
        'gazebos': gazebos,
        'garden_dining': garden_dining,
    }
    return render(request, 'dining/spaces.html', context)


def space_detail(request, slug):
    """Individual dining space detail"""
    space = get_object_or_404(
        DiningSpace.objects.prefetch_related('gallery'),
        slug=slug,
        is_active=True
    )
    
    # Get other spaces for related section
    related_spaces = DiningSpace.objects.filter(
        is_active=True
    ).exclude(id=space.id).order_by('display_order')[:3]
    
    context = {
        'space': space,
        'related_spaces': related_spaces,
    }
    return render(request, 'dining/space_detail.html', context)


def farm_to_fork_view(request):
    """Farm sources and sustainability"""
    page_settings = DiningPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = DiningPage.objects.create()
    
    farm_sources = FarmSource.objects.filter(
        is_active=True
    ).order_by('display_order')
    
    # Get food items sourced from farm
    farm_food = FoodItem.objects.filter(
        is_active=True,
        is_from_farm=True
    ).order_by('display_order')[:6]
    
    context = {
        'page_settings': page_settings,
        'farm_sources': farm_sources,
        'farm_food': farm_food,
    }
    return render(request, 'dining/farm_to_fork.html', context)
