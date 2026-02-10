# zamar_springs/apps/gardens/models.py
from django.db import models
from django.core.validators import MinValueValidator
from core.models import TimeStampedModel, SEOFields


class GardensPage(SEOFields, TimeStampedModel):
    """Main Gardens & Events landing page settings"""
    hero_title = models.CharField(
        max_length=200,
        default="Gardens & Events"
    )
    hero_subtitle = models.TextField(
        default="Beautiful garden venues for weddings, events, and celebrations in a serene, non-alcoholic environment"
    )
    intro_text = models.TextField(
        default="From intimate garden weddings to large corporate events, our beautifully maintained gardens provide the perfect backdrop for your special occasions."
    )
    is_active = models.BooleanField(default=True)
    
    # Why Choose Us Section
    why_title = models.CharField(
        max_length=200,
        default="Why Choose Our Gardens"
    )
    why_subtitle = models.TextField(
        default="Experience the perfect blend of natural beauty and professional event hosting"
    )
    
    class Meta:
        verbose_name = "Gardens Page Settings"
        verbose_name_plural = "Gardens Page Settings"
    
    def __str__(self):
        return "Gardens Page Settings"


class Garden(models.Model):
    """Individual garden venue"""
    GARDEN_TYPES = [
        ('main', 'Main Garden'),
        ('event', 'Event Garden'),
        ('special', 'Special Garden'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    garden_type = models.CharField(max_length=20, choices=GARDEN_TYPES)
    capacity = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Maximum capacity for events"
    )
    description = models.TextField()
    featured_image = models.ImageField(
        upload_to='gardens/',
        blank=True
    )
    
    # Features
    has_covered_area = models.BooleanField(default=True)
    has_power = models.BooleanField(default=True)
    has_lighting = models.BooleanField(default=True)
    has_restrooms = models.BooleanField(default=True)
    has_parking = models.BooleanField(default=True)
    is_wheelchair_accessible = models.BooleanField(default=True)
    
    # Dimensions
    area = models.CharField(max_length=100, blank=True)
    special_features = models.TextField(blank=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Garden"
        verbose_name_plural = "Gardens"
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - Capacity: {self.capacity}"


class EventType(SEOFields, TimeStampedModel):
    """Type of events (Weddings, Private Events, etc.)"""
    EVENT_CATEGORIES = [
        ('wedding', 'Weddings'),
        ('private', 'Private Events'),
        ('general', 'General Events'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    
    # Included services
    includes = models.TextField(
        help_text="Services included, one per line",
        blank=True
    )
    
    # Pricing info
    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Event Types"
        ordering = ['category', 'display_order']
    
    def __str__(self):
        return self.name


class EventGallery(models.Model):
    """Gallery images for events"""
    event_type = models.ForeignKey(
        EventType,
        on_delete=models.CASCADE,
        related_name='gallery'
    )
    image = models.ImageField(upload_to='gardens/events/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Event Gallery Image"
        verbose_name_plural = "Event Gallery Images"
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.event_type.name} - Image {self.display_order}"