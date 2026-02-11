from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.sitemaps import sitemaps

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    
    
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
