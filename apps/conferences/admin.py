from django.contrib import admin
from .models import (
    ConferencePage, ConferenceCategory, 
    ConferenceRoom, RoomGallery, ConferencePackage
)

@admin.register(ConferencePage)
class ConferencePageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active']
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Introduction', {
            'fields': ('intro_text',)
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        return not ConferencePage.objects.exists()

class RoomGalleryInline(admin.TabularInline):
    model = RoomGallery
    extra = 1
    fields = ('image', 'caption', 'display_order')
    ordering = ['display_order']

@admin.register(ConferenceCategory)
class ConferenceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['category_type', 'is_active']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'description']

@admin.register(ConferenceRoom)
class ConferenceRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'room_type', 'get_max_capacity', 'is_featured', 'is_active']
    list_filter = ['category', 'room_type', 'is_featured', 'is_active']
    list_editable = ['is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ['name']}
    inlines = [RoomGalleryInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug', 'room_type', 'description', 'featured_image')
        }),
        ('Capacity Layouts', {
            'fields': (
                'capacity_classroom', 'capacity_theatre', 'capacity_banquet',
                'capacity_u_shape', 'capacity_boardroom'
            )
        }),
        ('Amenities', {
            'fields': (
                'has_projector', 'has_sound_system', 'has_wifi',
                'has_whiteboard', 'has_air_conditioning', 'has_natural_light',
                'has_secretary_space', 'has_video_conferencing'
            )
        }),
        ('Dimensions & Pricing', {
            'fields': ('dimensions', 'floor_area', 'half_day_rate', 'full_day_rate', 'hourly_rate')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'display_order', 'is_active')
        }),
    )

@admin.register(ConferencePackage)
class ConferencePackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration', 'is_popular', 'is_active', 'display_order']
    list_editable = ['is_popular', 'is_active', 'display_order']
    list_filter = ['is_popular', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ['name']}
    
    fieldsets = (
        ('Package Information', {
            'fields': ('name', 'slug', 'description', 'includes', 'suitable_for')
        }),
        ('Pricing', {
            'fields': ('price', 'duration')
        }),
        ('Display Settings', {
            'fields': ('is_popular', 'display_order', 'is_active')
        }),
    )