from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db.models import Count

# Import models from other apps
try:
    from conferences.models import ConferenceRoom, ConferencePackage, ConferenceCategory
    from home.models import Feature, Service
except ImportError:
    # If imports fail, define empty classes or handle differently
    ConferenceRoom = ConferencePackage = ConferenceCategory = None
    Feature = Service = None

def staff_required(view_func):
    """Decorator to ensure user is staff member"""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url='/admin/login/'
    )
    return actual_decorator(view_func)

@staff_required
def dashboard(request):
    """Main admin dashboard"""
    # Get basic stats
    stats = {}
    
    if ConferenceRoom:
        total_rooms = ConferenceRoom.objects.count()
        active_rooms = ConferenceRoom.objects.filter(is_active=True).count()
        total_packages = ConferencePackage.objects.count() if ConferencePackage else 0
        total_categories = ConferenceCategory.objects.count() if ConferenceCategory else 0
    else:
        total_rooms = active_rooms = total_packages = total_categories = 0
    
    if Feature:
        total_features = Feature.objects.count()
        active_features = Feature.objects.filter(is_active=True).count()
        total_services = Service.objects.count() if Service else 0
    else:
        total_features = active_features = total_services = 0
    
    context = {
        'stats': {
            'conferences': {
                'total_rooms': total_rooms,
                'active_rooms': active_rooms,
                'total_packages': total_packages,
                'total_categories': total_categories,
            },
            'home': {
                'total_features': total_features,
                'active_features': active_features,
                'total_services': total_services,
            }
        },
        'active_module': 'dashboard',
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

@staff_required
def conference_dashboard(request):
    """Conference module dashboard"""
    if ConferenceRoom:
        rooms = ConferenceRoom.objects.all()
        room_stats = {
            'total': rooms.count(),
            'active': rooms.filter(is_active=True).count(),
            'featured': rooms.filter(is_featured=True).count(),
        }
    else:
        rooms = []
        room_stats = {'total': 0, 'active': 0, 'featured': 0}
    
    context = {
        'rooms': rooms[:5],  # Show only 5 recent rooms
        'room_stats': room_stats,
        'active_module': 'conferences',
    }
    
    return render(request, 'admin_dashboard/conferences/dashboard.html', context)

@staff_required
def home_dashboard(request):
    """Home module dashboard"""
    context = {
        'active_module': 'home',
    }
    
    return render(request, 'admin_dashboard/home/dashboard.html', context)

@staff_required
def system_dashboard(request):
    """System module dashboard"""
    context = {
        'active_module': 'system',
    }
    
    return render(request, 'admin_dashboard/system/dashboard.html', context)