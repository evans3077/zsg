from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import Http404, HttpResponse
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from home.sitemaps import sitemaps
from pathlib import Path


def tiktok_verification_file(request, filename):
    allowed_files = {
        "tiktokPCDNRc5372cRrCcX7sM5IrFWHOqhIv9e.txt",
    }
    if filename not in allowed_files:
        raise Http404("Verification file not found.")

    file_path = Path(settings.BASE_DIR) / "apps" / "conferences" / filename
    if not file_path.exists():
        raise Http404("Verification file not found.")

    return HttpResponse(file_path.read_text(encoding="utf-8"), content_type="text/plain; charset=utf-8")

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    re_path(r"^(tiktok[a-zA-Z0-9]+\.txt)$", tiktok_verification_file, name="tiktok_verification_file"),
    re_path(r"^conferences/(tiktok[a-zA-Z0-9]+\.txt)$", tiktok_verification_file, name="tiktok_verification_file_conferences"),
    
    
    path('', include('home.urls')),
    path('conferences/', include('conferences.urls')),
    path('gardens/', include('gardens.urls')), 
    path('dining/', include('dining.urls')),
    path('kids-family/', include('kids.urls')),
    path('gallery/', include('gallery.urls')),
    path('bookings/', include('bookings.urls')),
    path('manage/', include('admin_dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
