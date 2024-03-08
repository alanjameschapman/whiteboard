from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, School, Subject, Teacher, Set, Student, Enrolment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'subject', 'set', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')
    search_fields = ['user', 'school']
    list_filter = ('school',)

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'subject', 'school', 'year')
    search_fields = ['name', 'teacher', 'subject', 'school', 'year']
    list_filter = ('school', 'year')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'year', 'grade')
    search_fields = ['user', 'school', 'year', 'grade']
    list_filter = ('school', 'year', 'grade')

# Register your models here.
admin.site.register(Comment)
admin.site.register(School)
admin.site.register(Subject)
# admin.site.register(Teacher)
admin.site.register(Enrolment)
