from django.db import models

class TimeStampedModel(models.Model):
    """Abstract base model with created and updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # This is CRUCIAL - makes it abstract

class SEOFields(models.Model):
    """Abstract model for SEO fields."""
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(max_length=500, blank=True)
    meta_keywords = models.CharField(max_length=300, blank=True)
    
    class Meta:
        abstract = True  # This is CRUCIAL - makes it abstract