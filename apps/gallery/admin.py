from django.contrib import admin
from .models import GalleryPage, GalleryImage


@admin.register(GalleryPage)
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ["hero_title", "is_active", "updated_at"]
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle")}),
        ("SEO", {"fields": ("meta_title", "meta_description", "meta_keywords")}),
        ("Status", {"fields": ("is_active",)}),
    )

    def has_add_permission(self, request):
        return not GalleryPage.objects.exists()


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "display_order", "is_active"]
    list_filter = ["category", "is_active"]
    list_editable = ["display_order", "is_active"]
    search_fields = ["title", "alt_text", "caption", "image_path"]
