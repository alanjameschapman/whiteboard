"""
This file is used to create a form for the comment section of the blog.
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
