from django.shortcuts import render
from .models import HomePageSettings, Feature, Service

def home_view(request):
    # Get or create settings
    settings = HomePageSettings.objects.first()
    if not settings:
        settings = HomePageSettings.objects.create()
    
    # Get active features
    features = Feature.objects.filter(is_active=True).order_by('display_order')[:4]
    
    # Get active services
    services = Service.objects.filter(is_active=True).order_by('display_order')[:6]
    
    context = {
        'settings': settings,
        'features': features,
        'services': services,
    }
    
    return render(request, 'home/index.html', context)