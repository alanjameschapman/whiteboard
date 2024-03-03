# Generated by Django 5.0.2 on 2024-03-02 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edblog', '0003_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['post', '-created_on', 'author']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', 'author']},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edblog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]