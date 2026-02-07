from django.contrib import admin
from .models import HomePageSettings, Feature, Service

@admin.register(HomePageSettings)
class HomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'phone_number', 'email']
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Quick Stats', {
            'fields': ('years_experience', 'events_hosted', 'happy_customers')
        }),
        ('Features Section', {
            'fields': ('features_title', 'features_subtitle')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address', 'operating_hours')
        }),
    )
    
    def has_add_permission(self, request):
        return not HomePageSettings.objects.exists()

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']