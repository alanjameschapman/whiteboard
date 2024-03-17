"""
This file is used to create a form for the comment section of the blog.
"""
from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Post, STATUS


class CommentForm(forms.ModelForm):
    """
    A form for the comment section of the blog.
    **Fields**
    ``content``
        The content of the comment.
    """
    class Meta:
        """
        This class is used to create a form for the comment section of the blog.
        """
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    """
    A form for the blog post.
    **Fields**
    ``title``
        The title of the blog post.
    ``content``
        The content of the blog post.
    """
    content = forms.CharField(widget=SummernoteWidget())
    featured_image = forms.ImageField(required=False)
    status = forms.ChoiceField(choices=Post.STATUS)

    class Meta:
        """
        This class is used to create a form for the blog post.
        """
        model = Post
        fields = ('title', 'subject', 'set', 'featured_image', 'content', 'status')
