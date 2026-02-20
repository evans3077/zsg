from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Case, IntegerField, Value, When
from .models import (
    ConferencePage, ConferenceCategory, 
    ConferenceRoom, ConferencePackage
)


ROOM_TYPES_BY_CATEGORY_TYPE = {
    "board": ["board"],
    "meeting": ["executive", "standard"],
    "hall": ["hall"],
}


def _ordered_conference_categories_queryset():
    return (
        ConferenceCategory.objects.filter(
            is_active=True,
            category_type__in=["board", "meeting", "hall"],
        )
        .annotate(
            sort_priority=Case(
                When(category_type="board", then=Value(1)),
                When(category_type="meeting", then=Value(2)),
                When(category_type="hall", then=Value(3)),
                default=Value(99),
                output_field=IntegerField(),
            )
        )
        .order_by("sort_priority", "display_order", "name")
    )


def _room_type_filter_for_category(category):
    return ROOM_TYPES_BY_CATEGORY_TYPE.get(category.category_type, [])


def _attach_category_summaries(categories):
    for category in categories:
        room_type_filter = _room_type_filter_for_category(category)
        active_rooms = list(
            ConferenceRoom.objects.filter(
                is_active=True,
                room_type__in=room_type_filter,
            ).order_by("display_order", "name")
        )
        category.active_rooms = active_rooms
        if active_rooms:
            category.room_names_summary = ", ".join(room.name for room in active_rooms)
        else:
            category.room_names_summary = category.description
    return categories


def conference_overview(request):
    """Conference landing page"""
    page_settings = ConferencePage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = ConferencePage.objects.create()
    
    categories = list(_ordered_conference_categories_queryset())
    categories = _attach_category_summaries(categories)
    featured_rooms = (
        ConferenceRoom.objects.filter(is_active=True, is_featured=True)
        .select_related("category")
        .order_by('display_order')[:6]
    )
    popular_packages = ConferencePackage.objects.filter(is_active=True, is_popular=True).order_by('display_order')[:3]
    
    context = {
        'page_settings': page_settings,
        'categories': categories,
        'featured_rooms': featured_rooms,
        'popular_packages': popular_packages,
    }
    return render(request, 'conferences/overview.html', context)

def category_detail(request, slug):
    category = get_object_or_404(
        ConferenceCategory,
        slug=slug,
        is_active=True
    )
    room_type_filter = _room_type_filter_for_category(category)
    rooms = (
        ConferenceRoom.objects.filter(
            is_active=True,
            room_type__in=room_type_filter,
        )
        .select_related("category")
        .order_by('display_order', 'name')
    )

    all_categories = list(ConferenceCategory.objects.filter(
        id__in=_ordered_conference_categories_queryset().values("id")
    ).annotate(
        sort_priority=Case(
            When(category_type="board", then=Value(1)),
            When(category_type="meeting", then=Value(2)),
            When(category_type="hall", then=Value(3)),
            default=Value(99),
            output_field=IntegerField(),
        )
    ).order_by("sort_priority", "display_order", "name"))
    all_categories = _attach_category_summaries(all_categories)

    return render(request, 'conferences/category_detail.html', {
        'category': category,
        'rooms': rooms,
        'all_categories': all_categories,
    })





def room_detail(request, slug):
    room = get_object_or_404(
        ConferenceRoom.objects.select_related('category'),
        slug=slug,
        is_active=True
    )

    related_filter = ROOM_TYPES_BY_CATEGORY_TYPE.get(room.category.category_type, [room.room_type])
    related_rooms = (
        ConferenceRoom.objects.filter(
            is_active=True,
            room_type__in=related_filter,
        )
        .exclude(id=room.id)
        .order_by('display_order', 'name')[:3]
    )

    return render(request, 'conferences/room_detail.html', {
        'room': room,
        'related_rooms': related_rooms,
    })


def conference_packages(request):
    """All conference packages"""
    packages = ConferencePackage.objects.filter(is_active=True).order_by('display_order')
    popular_packages = packages.filter(is_popular=True)
    
    context = {
        'packages': packages,
        'popular_packages': popular_packages,
    }
    return render(request, 'conferences/packages.html', context)

def capacity_data(request, room_id):
    """API endpoint for room capacity data"""
    room = get_object_or_404(ConferenceRoom, id=room_id)
    
    data = {
        'classroom': room.capacity_classroom,
        'theatre': room.capacity_theatre,
        'banquet': room.capacity_banquet,
        'u_shape': room.capacity_u_shape,
        'boardroom': room.capacity_boardroom,
        'max_capacity': room.get_max_capacity(),
    }
    
    return JsonResponse(data)


def halls_category_redirect(request):
    halls_category = ConferenceCategory.objects.filter(is_active=True, category_type="hall").order_by("display_order", "name").first()
    if not halls_category:
        return redirect("conferences:overview")
    return redirect("conferences:category_detail", slug=halls_category.slug)
