# zamar_springs/apps/gardens/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import GardensPage, Garden, EventType

GARDEN_IMAGE_MAP = {
    "muuo-garden": "/static/images/web-pictures/muuo-grounds-zamarsprings.webp",
    "wendo-garden": "/static/images/web-pictures/wendo-events-gardens-machakos-2.webp",
    "utanu-garden": "/static/images/web-pictures/utanu-event-gardens-machakos.webp",
}

DEFAULT_GARDEN_IMAGE = "/static/images/web-pictures/garden-walkway-zamarsprings.webp"


def _decorate_garden(garden):
    if not garden:
        return None

    if garden.featured_image:
        garden.display_image = garden.featured_image.url
    else:
        garden.display_image = GARDEN_IMAGE_MAP.get(garden.slug, DEFAULT_GARDEN_IMAGE)
    return garden


def gardens_overview(request):
    """Gardens & Events landing page"""
    page_settings = GardensPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = GardensPage.objects.create()
    
    # Get featured gardens
    featured_gardens = Garden.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by('display_order')[:3]
    featured_gardens = [_decorate_garden(garden) for garden in featured_gardens]
    
    # Get all gardens
    gardens = Garden.objects.filter(is_active=True).order_by('display_order')
    gardens = [_decorate_garden(garden) for garden in gardens]
    
    # Get event types by category
    wedding_events = EventType.objects.filter(
        category='wedding',
        is_active=True
    ).order_by('display_order')
    
    private_events = EventType.objects.filter(
        category='private',
        is_active=True
    ).order_by('display_order')
    
    general_events = EventType.objects.filter(
        category='general',
        is_active=True
    ).order_by('display_order')
    
    context = {
        'page_settings': page_settings,
        'featured_gardens': featured_gardens,
        'gardens': gardens,
        'wedding_events': wedding_events,
        'private_events': private_events,
        'general_events': general_events,
    }
    return render(request, 'gardens/overview.html', context)


def weddings_view(request):
    """Weddings page"""
    event_types = EventType.objects.filter(
        category='wedding',
        is_active=True
    ).order_by('display_order')
    
    # Get gardens suitable for weddings
    wedding_gardens = Garden.objects.filter(
        is_active=True
    ).order_by('display_order')
    wedding_gardens = [_decorate_garden(garden) for garden in wedding_gardens]
    
    context = {
        'event_types': event_types,
        'gardens': wedding_gardens,
        'category': 'Weddings',
        'category_description': 'Beautiful garden weddings and receptions in our serene venues'
    }
    return render(request, 'gardens/category_detail.html', context)


def private_events_view(request):
    """Private Events page"""
    event_types = EventType.objects.filter(
        category='private',
        is_active=True
    ).order_by('display_order')
    
    context = {
        'event_types': event_types,
        'category': 'Private Events',
        'category_description': 'Celebrate your special moments with family and friends'
    }
    return render(request, 'gardens/category_detail.html', context)


def general_events_view(request):
    """General Events page"""
    event_types = EventType.objects.filter(
        category='general',
        is_active=True
    ).order_by('display_order')
    
    context = {
        'event_types': event_types,
        'category': 'General Events',
        'category_description': 'Corporate and group events in beautiful garden settings'
    }
    return render(request, 'gardens/category_detail.html', context)


def gardens_detail_view(request):
    """Gardens listing page"""
    gardens = Garden.objects.filter(is_active=True).order_by('display_order')
    gardens = [_decorate_garden(garden) for garden in gardens]
    
    context = {
        'gardens': gardens,
        'category': 'Our Gardens',
        'category_description': 'Explore our beautiful garden venues'
    }
    return render(request, 'gardens/gardens_detail.html', context)


def garden_detail(request, slug):
    """Individual garden detail page"""
    garden = get_object_or_404(Garden, slug=slug, is_active=True)
    garden = _decorate_garden(garden)
    
    # Get other gardens for related section
    related_gardens = Garden.objects.filter(
        is_active=True
    ).exclude(id=garden.id).order_by('display_order')[:3]
    related_gardens = [_decorate_garden(related) for related in related_gardens]
    
    # Get event types suitable for this garden
    suitable_events = EventType.objects.filter(
        is_active=True
    ).order_by('display_order')[:6]
    
    context = {
        'garden': garden,
        'related_gardens': related_gardens,
        'suitable_events': suitable_events,
    }
    return render(request, 'gardens/garden_detail.html', context)
