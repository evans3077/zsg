from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='index'),
    path("outdoor-events/", views.outdoor_events_view, name="outdoor_events"),
    path("careers/", views.careers_view, name="careers"),
    path("privacy-policy/", views.privacy_policy_view, name="privacy_policy"),
    path("terms-of-service/", views.terms_of_service_view, name="terms_of_service"),
    path("sitemap/", views.site_map_view, name="sitemap_page"),
    path("robots.txt", views.robots_txt_view, name="robots_txt"),
]
