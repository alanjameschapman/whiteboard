# Generated by Django 5.0.2 on 2024-03-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0005_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'unique': 'A post with this title already exists - please choose a different title. Case, punctuation and spacing are ignored.'}, max_length=200, unique=True),
        ),
    ]
