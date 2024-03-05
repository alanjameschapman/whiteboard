# Generated by Django 5.0.2 on 2024-03-05 06:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0004_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
