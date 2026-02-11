from datetime import date

from django.contrib import messages
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .models import BookingRequest


def _as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _as_date(value):
    try:
        return date.fromisoformat(value) if value else None
    except (TypeError, ValueError):
        return None


def _safe_next_url(request):
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        return next_url
    return "/"


@require_POST
def submit_booking(request):
    next_url = _safe_next_url(request)

    full_name = (request.POST.get("name") or "").strip()
    phone = (request.POST.get("phone") or "").strip()
    email = (request.POST.get("email") or "").strip()

    if not full_name or not phone:
        messages.error(request, "Full name and phone number are required.")
        return redirect(next_url)

    attendees = _as_int(request.POST.get("attendees") or request.POST.get("guests"))
    requested_date = _as_date(request.POST.get("event_date") or request.POST.get("date"))

    booking = BookingRequest.objects.create(
        request_type=request.POST.get("request_type") or "general",
        full_name=full_name,
        email=email,
        phone=phone,
        organization=(request.POST.get("company") or "").strip(),
        service_name=(
            request.POST.get("room")
            or request.POST.get("package")
            or request.POST.get("garden")
            or request.POST.get("space")
            or ""
        ).strip(),
        event_type=(request.POST.get("event_type") or "").strip(),
        attendees=attendees if attendees and attendees > 0 else None,
        requested_date=requested_date,
        requested_time=(request.POST.get("time") or "").strip(),
        budget=(request.POST.get("budget") or "").strip(),
        source_page=(request.POST.get("source_page") or request.path).strip(),
        message=(request.POST.get("message") or request.POST.get("notes") or "").strip(),
        raw_payload=request.POST.dict(),
    )

    messages.success(
        request,
        f"Request received. Reference #{booking.id}. Our team will contact you shortly.",
    )
    return redirect(next_url)
