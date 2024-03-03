from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on') # tailored to show latest and published posts first
    template_name = "edblog/index.html"
    paginate_by = 9 # Increased from 6 to 9. Consider tailoring for infinite scroll
