from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on') # tailored
    # to show latest and published posts first
    template_name = "edblog/index.html"
    paginate_by = 9 # Increased from 6 to 9. Infinite scroll discounted
    # because it tends to be used for aimless browsing - our users will be
    # looking for specific content. Last 9 posts should be enough to show, but
    # not too many to overwhelm the user.
