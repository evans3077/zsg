# zamar_springs/apps/gardens/context_processors.py
from .models import EventType

def gardens_categories(request):
    """Make gardens categories available in templates"""
    return {
        'gardens_categories': EventType.objects.filter(
            is_active=True
        ).order_by('category', 'display_order')
    }