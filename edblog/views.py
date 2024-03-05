from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


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

    **Template:**

    :template:`edblog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)  # pylint: disable=no-member
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
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
    print("About to render template")
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
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1) # pylint: disable=no-member
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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1) # pylint: disable=no-member
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user: # only allow the author to delete the comment
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
