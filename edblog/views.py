"""
Views for the :model:`edblog.Post` and :model:`edblog.Comment` models.
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create your views here.


class PostList(generic.ListView):
    """
    Display a list of :model:`blog.Post` objects.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # pylint: disable=no-member
    # tailored to show latest and published posts first
    template_name = "edblog/index.html"
    paginate_by = 9  # Increased from 6 to 9. Infinite scroll discounted
    # because it tends to be used for aimless browsing - our users will be
    # looking for specific content. Last 9 posts should be enough to show, but
    # not too many to overwhelm the user.


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
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


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

    if comment.author == request.user:  # only allow the author to delete the comment
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def create_post(request):
    """
    Create a new :model:`edblog.Post`.

    **Context**

    ``post_form``
        An instance of :form:`edblog.PostForm`.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save the form to the database yet
            post.author = request.user  # Set the author field to the current user
            post.save()  # Now save the form to the database
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'edblog/create_post.html', {'form': form})
