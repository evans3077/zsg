from django.http import HttpResponse
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


def privacy_policy_view(request):
    return render(request, "home/privacy_policy.html")


def terms_of_service_view(request):
    return render(request, "home/terms_of_service.html")


def site_map_view(request):
    sections = [
        {
            "title": "Main Pages",
            "links": [
                {"label": "Home", "url": "/"},
                {"label": "Conferences", "url": "/conferences/"},
                {"label": "Gardens & Events", "url": "/gardens/"},
                {"label": "Dining", "url": "/dining/"},
                {"label": "Kids & Family", "url": "/kids-family/"},
                {"label": "Gallery", "url": "/gallery/"},
            ],
        },
        {
            "title": "Important Pages",
            "links": [
                {"label": "Privacy Policy", "url": "/privacy-policy/"},
                {"label": "Terms of Service", "url": "/terms-of-service/"},
                {"label": "XML Sitemap", "url": "/sitemap.xml"},
            ],
        },
    ]
    return render(request, "home/sitemap.html", {"sections": sections})


def robots_txt_view(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: "
        f"{request.scheme}://{request.get_host()}/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")
