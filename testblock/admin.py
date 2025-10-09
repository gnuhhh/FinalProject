from django.contrib import admin
from .models import TestBlock, BlockQuestion, BlockTestResult

@admin.register(TestBlock)
class TestBlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    search_fields = ['name']

@admin.register(BlockQuestion)
class BlockQuestionAdmin(admin.ModelAdmin):
    list_display = ['test_block', 'text_short', 'correct_answer']
    list_filter = ['test_block']
    search_fields = ['text']
    
    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_short.short_description = 'Question Text'

@admin.register(BlockTestResult)
class BlockTestResultAdmin(admin.ModelAdmin):
    list_display = ['test_block', 'user_name', 'score', 'total_questions', 'percentage', 'created_at']
    list_filter = ['test_block', 'created_at']
    search_fields = ['user_name']
    readonly_fields = ['created_at']