# Generated by Django 5.0.2 on 2024-03-08 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0009_student_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edblog.subject'),
        ),
    ]
