from django.contrib import admin
from .models import Quote

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'submitted_by', 'created_at', 'is_approved']
    list_filter = ['is_approved', 'created_at', 'submitted_by']
    search_fields = ['text', 'author']
    list_editable = ['is_approved']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        return f"{obj.text[:100]}..." if len(obj.text) > 100 else obj.text
    text_preview.short_description = 'Quote Preview'
