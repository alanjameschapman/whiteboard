# Generated by Django 5.0.2 on 2024-03-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]