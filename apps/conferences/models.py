from django.db import models
from django.core.validators import MinValueValidator
from core.models import TimeStampedModel, SEOFields

class ConferencePage(SEOFields, TimeStampedModel):
    """Main conference landing page settings"""
    hero_title = models.CharField(max_length=200, default="Conference & Meetings")
    hero_subtitle = models.TextField(
        default="State-of-the-art meeting facilities in a serene, non-alcoholic environment"
    )
    intro_text = models.TextField(
        default="From intimate board meetings to large conferences, we have the perfect space for your business needs."
    )
    
    # Meta fields
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Conference Page Settings"
        verbose_name_plural = "Conference Page Settings"
    
    def __str__(self):
        return "Conference Page Settings"

class ConferenceCategory(models.Model):
    
    CATEGORY_TYPES = [
        ('board', 'Board Rooms'),
        ('meeting', 'Meeting Rooms'),
        ('hall', 'Meeting Hall'),
        ('training', 'Training & Workshops'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Conference Category"
        verbose_name_plural = "Conference Categories"
        ordering = ['display_order']
    
    def __str__(self):
        return self.name

class ConferenceRoom(SEOFields, TimeStampedModel):
    """Individual conference room/space"""
    ROOM_TYPES = [
        ('executive', 'Executive Room'),
        ('standard', 'Standard Room'),
        ('board', 'Board Room'),
        ('hall', 'Conference Hall'),
    ]
    
    category = models.ForeignKey(ConferenceCategory, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    description = models.TextField()
    
    # Capacity for different layouts
    capacity_classroom = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    capacity_theatre = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    capacity_banquet = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    capacity_u_shape = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    capacity_boardroom = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    
    # Features
    has_projector = models.BooleanField(default=True)
    has_sound_system = models.BooleanField(default=True)
    has_wifi = models.BooleanField(default=True)
    has_whiteboard = models.BooleanField(default=True)
    has_air_conditioning = models.BooleanField(default=True)
    has_natural_light = models.BooleanField(default=True)
    has_secretary_space = models.BooleanField(default=False)
    has_video_conferencing = models.BooleanField(default=False)
    
    # Dimensions
    dimensions = models.CharField(max_length=100, blank=True)
    floor_area = models.CharField(max_length=50, blank=True)
    
    # Pricing info
    half_day_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    full_day_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Images
    featured_image = models.ImageField(upload_to='conferences/rooms/', blank=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Conference Room"
        verbose_name_plural = "Conference Rooms"
        ordering = ['category', 'display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    def get_max_capacity(self):
        capacities = [
            self.capacity_classroom,
            self.capacity_theatre,
            self.capacity_banquet,
            self.capacity_u_shape,
            self.capacity_boardroom
        ]
        return max(capacities) if capacities else 0

class RoomGallery(models.Model):
    """Gallery images for conference rooms"""
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='conferences/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Room Gallery Image"
        verbose_name_plural = "Room Gallery Images"
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.room.name} - Image {self.display_order}"

class ConferencePackage(models.Model):
    """Pre-defined conference packages"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    includes = models.TextField(help_text="List package inclusions, one per line")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100, help_text="e.g., Half Day, Full Day")
    suitable_for = models.TextField(help_text="Ideal for which type of meetings")
    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Conference Package"
        verbose_name_plural = "Conference Packages"
        ordering = ['display_order']
    
    def __str__(self):
        return self.name