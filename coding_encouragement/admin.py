from django.contrib import admin
from django.utils import timezone
from .models import Quote

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'submitted_by', 'status', 'created_at', 'approved_by', 'is_approved']
    list_filter = ['is_approved', 'created_at', 'submitted_by', 'approved_by']
    search_fields = ['text', 'author', 'submitted_by__username']
    list_editable = ['is_approved']
    readonly_fields = ['created_at', 'approved_at', 'approved_by']
    actions = ['approve_quotes', 'reject_quotes']
    
    fieldsets = (
        ('Quote Content', {
            'fields': ('text', 'author', 'submitted_by')
        }),
        ('Approval Status', {
            'fields': ('is_approved', 'approved_at', 'approved_by'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def text_preview(self, obj):
        return f"{obj.text[:100]}..." if len(obj.text) > 100 else obj.text
    text_preview.short_description = 'Quote Preview'
    
    def status(self, obj):
        if obj.is_approved:
            return "✅ Approved"
        else:
            return "⏳ Pending Approval"
    status.short_description = 'Status'
    
    def approve_quotes(self, request, queryset):
        """Admin action to approve multiple quotes"""
        updated = 0
        for quote in queryset.filter(is_approved=False):
            quote.approve(request.user)
            updated += 1
        
        self.message_user(request, f'Successfully approved {updated} quote(s).')
    approve_quotes.short_description = "Approve selected quotes"
    
    def reject_quotes(self, request, queryset):
        """Admin action to reject (unapprove) multiple quotes"""
        updated = queryset.update(is_approved=False, approved_at=None, approved_by=None)
        self.message_user(request, f'Successfully rejected {updated} quote(s).')
    reject_quotes.short_description = "Reject selected quotes"
    
    def save_model(self, request, obj, form, change):
        """Override save to track who approved the quote"""
        if obj.is_approved and not obj.approved_by:
            obj.approved_at = timezone.now()
            obj.approved_by = request.user
        elif not obj.is_approved:
            obj.approved_at = None
            obj.approved_by = None
        super().save_model(request, obj, form, change)
