"""
This file is used to create a form for the comment section of the blog.
"""
from django import forms
from .models import Comment


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
