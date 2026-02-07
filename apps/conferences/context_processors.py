from .models import ConferenceCategory

def conference_categories(request):
    return {
        'conference_categories': ConferenceCategory.objects.filter(is_active=True).order_by('display_order')
    }
