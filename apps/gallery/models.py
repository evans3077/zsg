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


class SocialPost(TimeStampedModel):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("tiktok", "TikTok"),
        ("facebook", "Facebook"),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    post_id = models.CharField(max_length=120)
    caption = models.TextField(blank=True)
    media_url = models.URLField(max_length=500, blank=True)
    permalink = models.URLField(max_length=500)
    timestamp = models.DateTimeField()
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["platform", "-timestamp"]
        indexes = [
            models.Index(fields=["platform", "archived", "-timestamp"], name="gal_soc_p_a_ts_idx"),
            models.Index(fields=["post_id"], name="gal_soc_post_id_idx"),
        ]
        constraints = [
            models.UniqueConstraint(fields=["platform", "post_id"], name="unique_social_post_platform_id"),
        ]

    def __str__(self):
        return f"{self.get_platform_display()} - {self.post_id}"
