from django.contrib import admin

from .models import BookingRequest


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "request_type",
        "full_name",
        "phone",
        "service_name",
        "requested_date",
        "status",
    ]
    list_filter = ["request_type", "status", "created_at"]
    search_fields = ["full_name", "phone", "email", "organization", "service_name", "message"]
    readonly_fields = ["created_at", "updated_at", "raw_payload"]
