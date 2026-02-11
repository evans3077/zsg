# zamar_springs/apps/dining/views.py
from django.shortcuts import render, get_object_or_404
from .models import (
    DiningPage, FoodCategory, FoodItem,
    DiningSpace, FarmSource
)


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
    dining_spaces = DiningSpace.objects.filter(
        is_active=True
    ).prefetch_related('gallery').order_by('display_order')
    pergola_space = dining_spaces.filter(space_type='pergola').first()
    gazebo_spaces = dining_spaces.filter(space_type='gazebo')
    open_air_space = dining_spaces.filter(space_type='garden').first()
    
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
        items = FoodItem.objects.filter(
            category=category,
            is_active=True
        ).order_by('display_order')
        if items.exists():
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
