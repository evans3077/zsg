from django.db import models

from core.models import TimeStampedModel


class BookingRequest(TimeStampedModel):
    REQUEST_TYPES = [
        ("conference_room", "Conference Room Booking"),
        ("conference_package", "Conference Package Inquiry"),
        ("garden_event", "Garden Event Inquiry"),
        ("garden_booking", "Garden Booking"),
        ("dining_reservation", "Dining Reservation"),
        ("general", "General Inquiry"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("confirmed", "Confirmed"),
        ("closed", "Closed"),
    ]

    request_type = models.CharField(max_length=30, choices=REQUEST_TYPES, default="general")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    organization = models.CharField(max_length=200, blank=True)

    service_name = models.CharField(max_length=200, blank=True)
    event_type = models.CharField(max_length=120, blank=True)
    attendees = models.PositiveIntegerField(null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    requested_date = models.DateField(null=True, blank=True)
    requested_time = models.CharField(max_length=20, blank=True)
    budget = models.CharField(max_length=80, blank=True)

    source_page = models.CharField(max_length=250, blank=True)
    message = models.TextField(blank=True)
    raw_payload = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.full_name} ({self.phone})"
