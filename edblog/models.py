"""
This module contains the models for the edblog app.
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """

    title = models.CharField(
        max_length=200,
        unique=True,
        error_messages={
            'unique': 'A post with this title already exists - please choose a different title. Case, punctuation and spacing are ignored.',
        },)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edblog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        """
        Ensures that the slug is set using the title.
        """
        if not self.slug: # checks if the slug is set
            self.slug = slugify(self.title) # sets the slug using the title
        super(Post, self).save(*args, **kwargs)

    class Meta:
        """
        This class is used to create a model for the blog post entry.
        """
        ordering = ['-created_on', 'author']

    # pylint: disable=E0307
    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`edblog.Post` and :model:`auth.User`.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This class is used to create a model for the comment entry.
        """
        ordering = ['post', '-created_on', 'author']

    # pylint: disable=E0307
    def __str__(self):
        return self.content
