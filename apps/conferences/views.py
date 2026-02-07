from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import (
    ConferencePage, ConferenceCategory, 
    ConferenceRoom, ConferencePackage
)

def conference_overview(request):
    """Conference landing page"""
    page_settings = ConferencePage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = ConferencePage.objects.create()
    
    categories = ConferenceCategory.objects.filter(is_active=True).order_by('display_order')
    featured_rooms = ConferenceRoom.objects.filter(is_active=True, is_featured=True).order_by('display_order')[:6]
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
    rooms = ConferenceRoom.objects.filter(
        category=category,
        is_active=True
    ).order_by('display_order')

    all_categories = ConferenceCategory.objects.filter(
        is_active=True
    ).order_by('display_order')

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

    related_rooms = ConferenceRoom.objects.filter(
        category=room.category,
        is_active=True
    ).exclude(id=room.id).order_by('display_order')[:3]

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