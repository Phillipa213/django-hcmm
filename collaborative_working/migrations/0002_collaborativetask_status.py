# Generated by Django 5.1.2 on 2024-12-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborative_working', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborativetask',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('pending', 'Pending'), ('completed', 'Completed')], default='not_started', max_length=20),
        ),
    ]
