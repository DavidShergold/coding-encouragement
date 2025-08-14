from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Quote(models.Model):
    text = models.TextField(help_text="The motivational quote")
    author = models.CharField(max_length=100, blank=True, help_text="Quote author (optional)")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who submitted this quote")
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=True, help_text="Whether this quote is approved for display")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'"{self.text[:50]}..." - {self.author or "Unknown"}'
