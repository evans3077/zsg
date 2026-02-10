# zamar_springs/apps/gardens/admin.py - FIXED VERSION
from django.contrib import admin
from .models import GardensPage, Garden, EventType, EventGallery


@admin.register(GardensPage)
class GardensPageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active']
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'intro_text')
        }),
        ('Why Choose Us', {
            'fields': ('why_title', 'why_subtitle')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        return not GardensPage.objects.exists()


@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    list_display = ['name', 'garden_type', 'capacity', 'is_active', 'is_featured', 'display_order']
    list_filter = ['garden_type', 'is_active', 'is_featured']
    list_editable = ['is_active', 'is_featured', 'display_order']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'garden_type', 'description', 'featured_image')
        }),
        ('Capacity & Features', {
            'fields': ('capacity', 'area', 'special_features')
        }),
        ('Amenities', {
            'fields': (
                'has_covered_area',
                'has_power',
                'has_lighting',
                'has_restrooms',
                'has_parking',
                'is_wheelchair_accessible'
            )
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
    )


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'starting_price', 'is_active', 'is_featured', 'display_order']
    list_filter = ['category', 'is_active', 'is_featured']
    list_editable = ['is_active', 'is_featured', 'display_order']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'icon', 'description', 'detailed_description')
        }),
        ('Services & Pricing', {
            'fields': ('includes', 'starting_price')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
    )


@admin.register(EventGallery)
class EventGalleryAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'caption', 'display_order']
    list_filter = ['event_type']
    list_editable = ['display_order']