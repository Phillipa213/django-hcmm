from django import forms
from .models import CollaborativeTask

class CollaborativeTaskForm(forms.ModelForm):
    class Meta:
        model = CollaborativeTask
        fields = ['title', 'description', 'assigned_to', 'due_date', 'completed']
