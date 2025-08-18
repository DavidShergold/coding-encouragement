from django import template
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def smart_date(value):
    """
    Convert a datetime to a smart relative format:
    - Today: "Today"
    - Yesterday: "Yesterday" 
    - Within a week: "X days ago"
    - Older: "X weeks ago" or "X months ago"
    """
    if not value:
        return ""
    
    now = timezone.now()
    
    # Ensure both datetimes are timezone-aware or naive consistently
    if timezone.is_aware(now) and timezone.is_naive(value):
        value = timezone.make_aware(value)
    elif timezone.is_naive(now) and timezone.is_aware(value):
        value = timezone.make_naive(value)
    
    diff = now - value
    days = diff.days
    
    if days == 0:
        # Same day
        hours = diff.seconds // 3600
        if hours == 0:
            minutes = diff.seconds // 60
            if minutes == 0:
                return "Just now"
            elif minutes == 1:
                return "1 minute ago"
            else:
                return f"{minutes} minutes ago"
        elif hours == 1:
            return "1 hour ago"
        else:
            return f"{hours} hours ago"
    elif days == 1:
        return "Yesterday"
    elif days < 7:
        return f"{days} days ago"
    elif days < 30:
        weeks = days // 7
        if weeks == 1:
            return "1 week ago"
        else:
            return f"{weeks} weeks ago"
    elif days < 365:
        months = days // 30
        if months == 1:
            return "1 month ago"
        else:
            return f"{months} months ago"
    else:
        years = days // 365
        if years == 1:
            return "1 year ago"
        else:
            return f"{years} years ago"
