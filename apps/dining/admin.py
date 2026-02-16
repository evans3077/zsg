# zamar_springs/apps/dining/admin.py - FIXED VERSION
from django.contrib import admin
from .models import (
    DiningPage, FoodCategory, FoodItem,
    DiningSpace, SpaceGallery, FarmSource
)


@admin.register(DiningPage)
class DiningPageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active']
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'intro_text')
        }),
        ('Farm to Fork Section', {
            'fields': ('farm_title', 'farm_subtitle')
        }),
        ('Dining Spaces Section', {
            'fields': ('spaces_title', 'spaces_subtitle')
        }),
        ('Menu', {
            'fields': ('menu_title', 'menu_subtitle', 'menu_pdf')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        return not DiningPage.objects.exists()


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'display_order', 'is_active']
    list_filter = ['category_type', 'is_active']
    list_editable = ['display_order', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_from_farm', 'is_featured', 'is_special', 'display_order']  # Added is_special here
    list_filter = ['category', 'is_from_farm', 'is_featured', 'is_special', 'is_active']
    list_editable = ['is_featured', 'is_special', 'display_order']
    search_fields = ['name', 'description', 'search_tags', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description', 'search_tags', 'featured_image')
        }),
        ('Farm Connection', {
            'fields': ('is_from_farm', 'farm_ingredients')
        }),
        ('Pricing', {
            'fields': ('price',)
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_special', 'is_active', 'display_order')
        }),
    )


@admin.register(DiningSpace)
class DiningSpaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'space_type', 'capacity', 'is_featured', 'display_order']
    list_filter = ['space_type', 'is_featured', 'is_active']
    list_editable = ['is_featured', 'display_order']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'space_type', 'description', 'capacity')
        }),
        ('Ideal For', {
            'fields': ('ideal_for',)
        }),
        ('Features', {
            'fields': ('has_lighting', 'has_power', 'is_covered', 'is_private')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_active', 'display_order')
        }),
    )


@admin.register(SpaceGallery)
class SpaceGalleryAdmin(admin.ModelAdmin):
    list_display = ['dining_space', 'caption', 'display_order']
    list_filter = ['dining_space']
    list_editable = ['display_order']


@admin.register(FarmSource)
class FarmSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'source_type', 'display_order', 'is_active']
    list_filter = ['source_type', 'is_active']
    list_editable = ['display_order', 'is_active']
