from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
from .models import ConferenceRoom, ConferencePackage, ConferenceCategory

@staff_member_required
def conference_dashboard(request):
    """Custom dashboard for conference management"""
    # Get statistics
    total_rooms = ConferenceRoom.objects.count()
    active_rooms = ConferenceRoom.objects.filter(is_active=True).count()
    featured_rooms = ConferenceRoom.objects.filter(is_featured=True).count()
    
    total_packages = ConferencePackage.objects.count()
    popular_packages = ConferencePackage.objects.filter(is_popular=True).count()
    
    total_categories = ConferenceCategory.objects.count()
    
    # Get rooms by category
    rooms_by_category = ConferenceCategory.objects.annotate(
        room_count=Count('rooms'),
        active_rooms=Count('rooms', filter=models.Q(rooms__is_active=True))
    ).order_by('display_order')
    
    # Recent activity (last 7 days)
    week_ago = timezone.now() - timedelta(days=7)
    
    context = {
        'total_rooms': total_rooms,
        'active_rooms': active_rooms,
        'featured_rooms': featured_rooms,
        'total_packages': total_packages,
        'popular_packages': popular_packages,
        'total_categories': total_categories,
        'rooms_by_category': rooms_by_category,
        'stats': {
            'rooms_active_percentage': (active_rooms / total_rooms * 100) if total_rooms > 0 else 0,
            'packages_popular_percentage': (popular_packages / total_packages * 100) if total_packages > 0 else 0,
        }
    }
    
    return render(request, 'conferences/admin/dashboard.html', context)