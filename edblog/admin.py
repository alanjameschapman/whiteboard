"""
This file is used to configure the edblog admin pages.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Post, Comment, School, Subject,
    Teacher, Set, Student, Enrolment
)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''Admin View for Post'''
    list_display = (
        'title', 'author', 'subject',
        'set', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''
    list_display = ('user', 'school')
    search_fields = ['user', 'school']
    list_filter = ('school',)


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    '''Admin View for Set'''
    list_display = ('name', 'teacher', 'subject', 'school', 'year')
    search_fields = ['name', 'teacher', 'subject', 'school', 'year']
    list_filter = ('school', 'year')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''
    list_display = ('user', 'school', 'year', 'grade')
    search_fields = ['user', 'school', 'year', 'grade']
    list_filter = ('school', 'year', 'grade')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''
    list_display = ('post', 'author', 'content', 'created_on', 'approved')
    search_fields = ['author', 'content']
    list_filter = ('approved', 'author')

    actions = ['approve_comments']

    def approve_comments(self, _request, queryset):
        '''Approve selected comments'''
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"


# Register your models here.
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Enrolment)
