from django.db import models
from core.models import SEOFields, TimeStampedModel


class GalleryPage(SEOFields, TimeStampedModel):
    hero_title = models.CharField(max_length=200, default="Hotel Gallery")
    hero_subtitle = models.TextField(
        default="Explore weddings, events, dining, kids activities, and outdoor spaces at Zamar Springs Gardens."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gallery Page Settings"
        verbose_name_plural = "Gallery Page Settings"

    def __str__(self):
        return "Gallery Page Settings"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ("weddings", "Weddings & Special Events"),
        ("conferences", "Conferences & Corporate Events"),
        ("dining", "Dining & Farm-to-Fork Experience"),
        ("kids_family", "Kids & Family Fun"),
        ("gardens", "Gardens & Outdoor Spaces"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image_path = models.CharField(
        max_length=300,
        help_text="Absolute static/media path, e.g. /static/images/gallery/file.webp",
    )
    alt_text = models.CharField(max_length=250)
    caption = models.CharField(max_length=280, blank=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "display_order", "title"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
