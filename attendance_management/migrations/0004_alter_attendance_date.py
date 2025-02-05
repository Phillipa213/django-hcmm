# Generated by Django 5.1.2 on 2024-12-03 00:46

import attendance_management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_management', '0003_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(validators=[attendance_management.models.validate_date_not_future]),
        ),
    ]
