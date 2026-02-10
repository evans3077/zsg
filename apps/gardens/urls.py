# zamar_springs/apps/gardens/urls.py
from django.urls import path
from . import views

app_name = 'gardens'

urlpatterns = [
    path('', views.gardens_overview, name='overview'),
    path('weddings/', views.weddings_view, name='weddings'),
    path('private-events/', views.private_events_view, name='private_events'),
    path('general-events/', views.general_events_view, name='general_events'),
    path('gardens/', views.gardens_detail_view, name='gardens_list'),
    path('garden/<slug:slug>/', views.garden_detail, name='garden_detail'),
]