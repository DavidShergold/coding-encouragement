from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Quote, Report

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'submitted_by', 'status', 'report_count', 'created_at', 'approved_by', 'is_approved']
    list_filter = ['is_approved', 'is_hidden', 'created_at', 'submitted_by', 'approved_by']
    search_fields = ['text', 'author', 'submitted_by__username']
    list_editable = ['is_approved']
    readonly_fields = ['created_at', 'approved_at', 'approved_by', 'report_count']
    actions = ['approve_quotes', 'reject_quotes', 'hide_quotes', 'unhide_quotes']
    
    fieldsets = (
        ('Quote Content', {
            'fields': ('text', 'author', 'submitted_by')
        }),
        ('Approval Status', {
            'fields': ('is_approved', 'approved_at', 'approved_by'),
            'classes': ('collapse',)
        }),
        ('Moderation', {
            'fields': ('is_hidden', 'report_count'),
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
        if obj.is_hidden:
            return format_html('<span style="color: red;">🚫 Hidden</span>')
        elif obj.is_approved:
            return format_html('<span style="color: green;">✅ Approved</span>')
        else:
            return format_html('<span style="color: orange;">⏳ Pending</span>')
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
    
    def hide_quotes(self, request, queryset):
        """Admin action to hide multiple quotes"""
        updated = queryset.update(is_hidden=True)
        self.message_user(request, f'Successfully hidden {updated} quote(s).')
    hide_quotes.short_description = "Hide selected quotes"
    
    def unhide_quotes(self, request, queryset):
        """Admin action to unhide multiple quotes"""
        updated = queryset.update(is_hidden=False)
        self.message_user(request, f'Successfully unhidden {updated} quote(s).')
    unhide_quotes.short_description = "Unhide selected quotes"
    
    def save_model(self, request, obj, form, change):
        """Override save to track who approved the quote"""
        if obj.is_approved and not obj.approved_by:
            obj.approved_at = timezone.now()
            obj.approved_by = request.user
        elif not obj.is_approved:
            obj.approved_at = None
            obj.approved_by = None
        super().save_model(request, obj, form, change)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['quote_preview', 'reported_by', 'reason', 'status', 'created_at', 'resolved_by']
    list_filter = ['reason', 'is_resolved', 'created_at', 'resolved_by']
    search_fields = ['quote__text', 'reported_by__username', 'description']
    readonly_fields = ['created_at', 'resolved_at', 'resolved_by']
    actions = ['resolve_reports', 'unresolve_reports']
    
    fieldsets = (
        ('Report Details', {
            'fields': ('quote', 'reported_by', 'reason', 'description')
        }),
        ('Resolution', {
            'fields': ('is_resolved', 'resolved_at', 'resolved_by'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def quote_preview(self, obj):
        return f'"{obj.quote.text[:60]}..." by {obj.quote.author or "Unknown"}'
    quote_preview.short_description = 'Reported Quote'
    
    def status(self, obj):
        if obj.is_resolved:
            return format_html('<span style="color: green;">✅ Resolved</span>')
        else:
            return format_html('<span style="color: red;">🔴 Open</span>')
    status.short_description = 'Status'
    
    def resolve_reports(self, request, queryset):
        """Admin action to resolve multiple reports"""
        updated = 0
        for report in queryset.filter(is_resolved=False):
            report.resolve(request.user)
            updated += 1
        
        self.message_user(request, f'Successfully resolved {updated} report(s).')
    resolve_reports.short_description = "Resolve selected reports"
    
    def unresolve_reports(self, request, queryset):
        """Admin action to unresolve multiple reports"""
        updated = queryset.update(is_resolved=False, resolved_at=None, resolved_by=None)
        self.message_user(request, f'Successfully unresolved {updated} report(s).')
    unresolve_reports.short_description = "Unresolve selected reports"
