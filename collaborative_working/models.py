from django.db import models
from emp_management.models import Employee

class CollaborativeTask(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')  # Added status field
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

