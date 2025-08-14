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
    is_hidden = models.BooleanField(default=False, help_text="Whether this quote is hidden due to reports")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        if self.is_hidden:
            status = "🚫 Hidden"
        elif self.is_approved:
            status = "✅ Approved"
        else:
            status = "⏳ Pending"
        return f'"{self.text[:50]}..." - {self.author or "Unknown"} ({status})'
    
    def approve(self, approved_by_user):
        """Approve the quote and record who approved it and when"""
        self.is_approved = True
        self.approved_at = timezone.now()
        self.approved_by = approved_by_user
        self.save()
    
    def report_count(self):
        """Get the number of reports for this quote"""
        return self.reports.count()
    
    def check_auto_hide(self):
        """Automatically hide quote if it has 3 or more reports"""
        if self.report_count() >= 3:
            self.is_hidden = True
            self.save()


class Report(models.Model):
    REPORT_REASONS = [
        ('inappropriate', 'Inappropriate Content'),
        ('offensive', 'Offensive Language'),
        ('spam', 'Spam'),
        ('copyright', 'Copyright Violation'),
        ('other', 'Other'),
    ]
    
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='reports')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REPORT_REASONS)
    description = models.TextField(blank=True, help_text="Additional details about the report")
    created_at = models.DateTimeField(default=timezone.now)
    is_resolved = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_reports')
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['quote', 'reported_by']  # Prevent duplicate reports from same user
    
    def __str__(self):
        return f'Report by {self.reported_by.username} for quote "{self.quote.text[:30]}..."'
    
    def resolve(self, resolved_by_user):
        """Mark the report as resolved"""
        self.is_resolved = True
        self.resolved_by = resolved_by_user
        self.resolved_at = timezone.now()
        self.save()
