from django.urls import path
from . import views

app_name = 'conferences'

urlpatterns = [
    path('', views.conference_overview, name='overview'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('room/<slug:slug>/', views.room_detail, name='room_detail'),
    path('packages/', views.conference_packages, name='packages'),
    path('api/capacity/<int:room_id>/', views.capacity_data, name='capacity_data'),
]