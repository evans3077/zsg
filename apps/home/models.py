from django.db import models
from django.core.validators import MinValueValidator

class HomePageSettings(models.Model):
    """Settings for the homepage."""
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Zamar Springs Gardens")
    hero_subtitle = models.TextField(
        default="A serene, non-alcoholic garden venue for conferences, events, dining and family fun - located in Mua Hills, Machakos"
    )
    
    # Quick Stats
    years_experience = models.IntegerField(default=2, validators=[MinValueValidator(0)])
    events_hosted = models.IntegerField(default=200, validators=[MinValueValidator(0)])
    happy_customers = models.IntegerField(default=2000, validators=[MinValueValidator(0)])
    
    # Features Section
    features_title = models.CharField(max_length=200, default="Why Choose Zamar Springs?")
    features_subtitle = models.TextField(
        blank=True,
        default="Discover our unique offerings that make us the perfect choice for your events"
    )
    
    # Contact Info
    phone_number = models.CharField(max_length=20, default="0112394681")
    email = models.EmailField(default="info@zamarsprings.com")
    address = models.TextField(
        default="Kithini, Machakos, 45 minutes from Nairobi CBD"
    )
    operating_hours = models.TextField(
        default="Open Daily: 8:00 AM - 10:00 PM"
    )
    
    class Meta:
        verbose_name = "Home Page Settings"
        verbose_name_plural = "Home Page Settings"
    
    def __str__(self):
        return "Home Page Settings"

class Feature(models.Model):
    """Features displayed on homepage."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.title

class Service(models.Model):
    """Services preview on homepage."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.name