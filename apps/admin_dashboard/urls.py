from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    # Main dashboard: /manage/
    path('', views.dashboard, name='dashboard'),
    
    # Conference dashboard: /manage/conferences/
    path('conferences/', views.conference_dashboard, name='conference_dashboard'),
    
    # Home dashboard: /manage/home/
    path('home/', views.home_dashboard, name='home_dashboard'),
    
    # System dashboard: /manage/system/
    path('system/', views.system_dashboard, name='system_dashboard'),
]