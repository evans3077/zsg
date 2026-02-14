from django.db.models import Case, IntegerField, Value, When

from .models import ConferenceCategory


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

def conference_categories(request):
    return {
        "conference_categories": _ordered_conference_categories_queryset()
    }
