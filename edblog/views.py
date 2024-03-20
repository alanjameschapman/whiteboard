"""
Views for the :model:`edblog.Post` and :model:`edblog.Comment` models.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.defaultfilters import slugify
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment, Enrolment
from .forms import CommentForm, PostForm


class PostList(LoginRequiredMixin, generic.ListView):
    """
    Display a list of :model:`blog.Post` objects.
    """
    # tailored to show relevant posts to the user
    model = Post
    template_name = "edblog/index.html"
    paginate_by = 9

    def get_queryset(self):
        # Check if the user has a related Teacher instance
        if hasattr(self.request.user, 'teacher'):
            # Get the posts authored by the teacher
            return Post.objects.filter( # pylint: disable=no-member
                author=self.request.user).order_by('-created_on')
        elif hasattr(self.request.user, 'student'):
            # Get the enrolments for the student
            enrolments = Enrolment.objects.filter( # pylint: disable=no-member
                student=self.request.user.student)
            # Get the sets and subjects from the enrolments
            student_sets = [enrolment.set for enrolment in enrolments]
            student_subjects = [enrolment.subject for enrolment in enrolments]
            # Get the posts related to the sets and subjects from the enrolments
            return (
                Post.objects.filter( # pylint: disable=no-member
                    set__in=student_sets,
                    subject__in=student_subjects,
                    status=1
                )
                .order_by('-created_on')
            )
        else:
            # If the user has neither a related Teacher nor Student instance,
            # return an empty queryset
            return Post.objects.none() # pylint: disable=no-member


# Django's generic view for updating a model instance
class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update a :model:`edblog.Post`.
    """
    model = Post
    template_name = 'edblog/create_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.slug])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a :model:`edblog.Post`.
    """
    model = Post
    success_url = reverse_lazy('home')  # replace with your post list URL

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


@login_required
def post_detail(request, slug):
    """
    Display an individual :model:`edblog.Post`.

    **Context**

    ``post``
        An instance of :model:`edblog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        The number of approved comments related to the post.
    ``comment_form``
        An instance of :form:`edblog.CommentForm`.

    **Template:**

    :template:`edblog/post_detail.html`
    """

    # If the user is a teacher, they can see all posts
    if hasattr(request.user, 'teacher'):
        queryset = Post.objects.all()  # pylint: disable=no-member
    # Otherwise, only show published posts
    else:
        queryset = Post.objects.filter(status=1)  # pylint: disable=no-member

    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            # If the user is a teacher, automatically approve the comment
            if hasattr(request.user, 'teacher'):
                comment.approved = True
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    return render(
        request,
        "edblog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    Display an individual :model:`edblog.Comment` for editing.

    **Context**

    ``post``
        An instance of :model:`edblog.Post`.
    ``comment``
        An instance of :model:`edblog.Comment`.
    ``comment_form``
        An instance of :form:`edblog.CommentForm`.
    """

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)  # pylint: disable=no-member
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            if hasattr(request.user, 'teacher'):  # check if user is teacher
                comment.approved = True
            else:
                comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual :model:`edblog.Comment`.

    **Context**

    ``post``
        An instance of :model:`edblog.Post`.
    ``comment``
        An instance of :model:`edblog.Comment`.

    """
    queryset = Post.objects.filter(status=1)  # pylint: disable=no-member
    post = get_object_or_404(queryset, slug=slug)  # pylint: disable=unused-variable
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:  # only allow  author to delete comment
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def create_post(request):
    """
    Create a new :model:`edblog.Post`.

    **Context**

    ``post_form``
        An instance of :form:`edblog.PostForm`.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Don't save the form to the database yet
            post = form.save(commit=False)
            post.author = request.user  # Set author field to current user
            post.slug = slugify(post.title)
            # Set the status based on the form input
            post.status = form.cleaned_data['status']
            try:
                post.save()  # Try to save the form to the database
            except IntegrityError as e:  # If slug not unique, add form error
                if 'slug' in str(e):
                    form.add_error('title', 'A post with this title already '
                                   'exists - please choose a different title.'
                                   ' Case, punctuation and spacing are '
                                   'ignored.')
                    return render(
                        request,
                        'edblog/create_post.html',
                        {'form': form})
                raise e
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'edblog/create_post.html', {'form': form})


def custom_404(request, exception):
    """
    Custom 404 error page.
    """
    return render(request, '404.html', status=404)


@csrf_exempt
def comment_approve(request, comment_id):
    """
    Approve an individual :model:`edblog.Comment`.

    **Context**

    ``post``
        An instance of :model:`edblog.Post`.
    ``comment``
        An instance of :model:`edblog.Comment`.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.approved = True
        comment.save()
        return JsonResponse({'success': True})
    else:
        return HttpResponse('Invalid request method', status=405)
