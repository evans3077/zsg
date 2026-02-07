from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AdminActivity(models.Model):
    """Track admin activities across the site"""
    ACTIVITY_TYPES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('view', 'View'),
        ('login', 'Login'),
        ('logout', 'Logout'),
    ]
    
    MODULE_CHOICES = [
        ('conferences', 'Conferences'),
        ('home', 'Home'),
        ('gardens', 'Gardens'),
        ('dining', 'Dining'),
        ('kids', 'Kids'),
        ('bookings', 'Bookings'),
        ('gallery', 'Gallery'),
        ('packages', 'Packages'),
        ('contact', 'Contact'),
        ('about', 'About'),
        ('system', 'System'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    module = models.CharField(max_length=50, choices=MODULE_CHOICES)
    description = models.TextField()
    model_name = models.CharField(max_length=100, blank=True)
    object_id = models.IntegerField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Admin Activity"
        verbose_name_plural = "Admin Activities"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user} - {self.activity_type} - {self.module}"

class AdminNotification(models.Model):
    """Notifications for admin users"""
    NOTIFICATION_TYPES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('success', 'Success'),
    ]
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    module = models.CharField(max_length=50, choices=AdminActivity.MODULE_CHOICES)
    is_read = models.BooleanField(default=False)
    action_url = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Admin Notification"
        verbose_name_plural = "Admin Notifications"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False

class QuickLink(models.Model):
    """Quick links for admin dashboard"""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=500)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    module = models.CharField(max_length=50, choices=AdminActivity.MODULE_CHOICES)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Quick Link"
        verbose_name_plural = "Quick Links"
        ordering = ['module', 'display_order']
    
    def __str__(self):
        return self.title