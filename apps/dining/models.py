# zamar_springs/apps/dining/models.py
from django.db import models
from django.core.validators import MinValueValidator
from core.models import TimeStampedModel, SEOFields


class DiningPage(SEOFields, TimeStampedModel):
    """Main Dining landing page settings"""
    hero_title = models.CharField(
        max_length=200,
        default="Dining Experience"
    )
    hero_subtitle = models.TextField(
        default="Farm-to-fork dining in a serene, non-alcoholic environment"
    )
    intro_text = models.TextField(
        default="Experience fresh, organic meals prepared with ingredients from our own farm. Enjoy dining in our beautiful pergolas and gazebos surrounded by nature."
    )
    
    # Farm to Fork Section
    farm_title = models.CharField(
        max_length=200,
        default="Farm-to-Fork Freshness"
    )
    farm_subtitle = models.TextField(
        default="All ingredients sourced directly from our organic farm"
    )
    
    # Dining Spaces Section
    spaces_title = models.CharField(
        max_length=200,
        default="Prime Dining Spaces"
    )
    spaces_subtitle = models.TextField(
        default="Beautiful locations for memorable dining experiences"
    )
    
    # Menu
    menu_pdf = models.FileField(
        upload_to='dining/menus/',
        blank=True,
        help_text="Upload PDF menu file"
    )
    menu_title = models.CharField(
        max_length=200,
        default="Our Menu"
    )
    menu_subtitle = models.TextField(
        default="Fresh, organic, and delicious"
    )
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Dining Page Settings"
        verbose_name_plural = "Dining Page Settings"
    
    def __str__(self):
        return "Dining Page Settings"


class FoodCategory(models.Model):
    """Categories for organizing food items"""
    CATEGORY_TYPES = [
        ('juices', 'Fresh Juices'),
        ('mocktails', 'Mocktails & Coffee'),
        ('platters', 'Platters'),
        ('mains', 'Main Dishes'),
        ('bbq', 'BBQ / Choma Zone'),
        ('desserts', 'Desserts'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=50,
        help_text="Font Awesome icon class"
    )
    
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Food Category"
        verbose_name_plural = "Food Categories"
        ordering = ['display_order']
    
    def __str__(self):
        return self.name


class FoodItem(SEOFields, TimeStampedModel):
    """Individual food/drink items"""
    category = models.ForeignKey(
        FoodCategory,
        on_delete=models.CASCADE,
        related_name='food_items'
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="Brief description of the dish")
    
    # Ingredients sourced from farm
    is_from_farm = models.BooleanField(default=False)
    farm_ingredients = models.TextField(
        blank=True,
        help_text="List farm-sourced ingredients, one per line"
    )
    
    # Pricing (optional as per requirements)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Optional - price can be shown subtly or not at all"
    )
    
    # Images
    featured_image = models.ImageField(
        upload_to='dining/food/',
        blank=True,
        help_text="High-quality food photo"
    )
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False, help_text="Chef's special")
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"
        ordering = ['category', 'display_order']
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    def get_farm_ingredients_list(self):
        """Return farm ingredients as list"""
        if self.farm_ingredients:
            return [ing.strip() for ing in self.farm_ingredients.split('\n') if ing.strip()]
        return []


class DiningSpace(models.Model):
    """Special dining locations (Pergola, Gazebos)"""
    SPACE_TYPES = [
        ('pergola', 'Pergola'),
        ('gazebo', 'Gazebo'),
        ('garden', 'Garden Dining'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    space_type = models.CharField(max_length=20, choices=SPACE_TYPES)
    description = models.TextField()
    capacity = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of people"
    )
    
    # Ideal for
    ideal_for = models.TextField(
        help_text="Ideal occasions, one per line"
    )
    
    # Features
    has_lighting = models.BooleanField(default=True)
    has_power = models.BooleanField(default=True)
    is_covered = models.BooleanField(default=True)
    is_private = models.BooleanField(default=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Dining Space"
        verbose_name_plural = "Dining Spaces"
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.name} - {self.get_space_type_display()}"
    
    def get_ideal_for_list(self):
        """Return ideal occasions as list"""
        if self.ideal_for:
            return [item.strip() for item in self.ideal_for.split('\n') if item.strip()]
        return []


class SpaceGallery(models.Model):
    """Gallery images for dining spaces"""
    dining_space = models.ForeignKey(
        DiningSpace,
        on_delete=models.CASCADE,
        related_name='gallery'
    )
    image = models.ImageField(upload_to='dining/spaces/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Space Gallery Image"
        verbose_name_plural = "Space Gallery Images"
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.dining_space.name} - Image {self.display_order}"


class FarmSource(models.Model):
    """Sources from our farm"""
    SOURCE_TYPES = [
        ('vegetable', 'Vegetables'),
        ('fruit', 'Fruits'),
        ('herb', 'Herbs'),
        ('meat', 'Meat'),
        ('dairy', 'Dairy'),
    ]
    
    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField()
    image = models.ImageField(upload_to='dining/farm/', blank=True)
    
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Farm Source"
        verbose_name_plural = "Farm Sources"
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.name} - {self.get_source_type_display()}"
