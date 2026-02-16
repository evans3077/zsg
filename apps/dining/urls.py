# zamar_springs/apps/dining/urls.py
from django.urls import path
from . import views

app_name = 'dining'

urlpatterns = [
    path('', views.dining_overview, name='overview'),
    path('api/search/', views.menu_search_api, name='menu_search_api'),
    path('menu/', views.menu_view, name='menu'),
    path('dining-spaces/', views.dining_spaces_view, name='spaces'),
    path('space/<slug:slug>/', views.space_detail, name='space_detail'),
    path('farm-to-fork/', views.farm_to_fork_view, name='farm_to_fork'),
]
