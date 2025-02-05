from django.contrib import admin
from .models import CollaborativeTask

@admin.register(CollaborativeTask)
class CollaborativeTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'due_date', 'completed')
    search_fields = ('title', 'assigned_to__name')
