from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Quote(models.Model):
    text = models.TextField(help_text="The motivational quote")
    author = models.CharField(max_length=100, blank=True, help_text="Quote author (optional)")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who submitted this quote")
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False, help_text="Whether this quote is approved for display")
    approved_at = models.DateTimeField(null=True, blank=True, help_text="When this quote was approved")
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_quotes', help_text="Admin who approved this quote")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        status = "✅ Approved" if self.is_approved else "⏳ Pending"
        return f'"{self.text[:50]}..." - {self.author or "Unknown"} ({status})'
    
    def approve(self, approved_by_user):
        """Approve the quote and record who approved it and when"""
        self.is_approved = True
        self.approved_at = timezone.now()
        self.approved_by = approved_by_user
        self.save()
