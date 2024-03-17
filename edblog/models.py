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

    # used to set the status of the post 
    STATUS = ((0, "Draft"), (1, "Published"))
    
    title = models.CharField(
        max_length=200,
        unique=True,
        error_messages={
            'unique': 'A post with this title already exists - please choose a different title. Case, punctuation and spacing are ignored.',
        },)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edblog_posts')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    set = models.ForeignKey('Set', on_delete=models.CASCADE, blank=True, null=True)
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


class School(models.Model):
    """
    Stores a single school entry.
    """

    name = models.CharField(max_length=200)

    class Meta:
        """
        This class is used to create a model for the school entry.
        """
        ordering = ['name']

    # pylint: disable=E0307
    def __str__(self):
        return self.name


class Subject(models.Model):
    """
    Stores a single subject entry.
    """

    name = models.CharField(max_length=200)

    class Meta:
        """
        This class is used to create a model for the subject entry.
        """
        ordering = ['name']

    # pylint: disable=E0307
    def __str__(self):
        return self.name


class Teacher(models.Model):
    """
    Stores a single teacher entry related to :model:`edblog.School`.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        """
        This class is used to create a model for the teacher entry.
        """
        ordering = ['school', 'user']

    # pylint: disable=E0307
    def __str__(self):
        return self.user.username # pylint: disable=no-member


class Set(models.Model):
    """
    Stores a single set entry related to :model:`edblog.Subject`.
    """

    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()

    class Meta:
        """
        This class is used to create a model for the set entry.
        """
        ordering = ['subject', 'name']

    # pylint: disable=E0307
    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Stores a single student entry related to :model:`edblog.School`.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    grade = models.IntegerField()
    sets = models.ManyToManyField(Set, through='Enrolment')

    class Meta:
        """
        This class is used to create a model for the student entry.
        """
        ordering = ['user__username']

    # pylint: disable=E0307
    def __str__(self):
        return self.user.username # pylint: disable=no-member


class Enrolment(models.Model):
    """
    Stores a single enrolment entry related to :model:`edblog.Student` and :model:`edblog.Subject`.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        """
        This class is used to create a model for the enrolment entry.
        """
        ordering = ['student', 'subject']

    # pylint: disable=E0307
    def __str__(self):
        return self.student.user.username + " studying " + self.subject.name + " in " + self.set.name + " taught by " + self.set.teacher.user.username # pylint: disable=no-member
