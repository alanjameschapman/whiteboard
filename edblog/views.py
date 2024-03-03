from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    """
    Display a list of :model:`blog.Post` objects.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on') # pylint: disable=no-member
    # tailored to show latest and published posts first
    template_name = "edblog/index.html"
    paginate_by = 9 # Increased from 6 to 9. Infinite scroll discounted
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

    queryset = Post.objects.filter(status=1) # pylint: disable=no-member
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "edblog/post_detail.html",
        {"post": post},
    )
