from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as_view() required for class-based views.
    path('<slug:slug>/', views.post_detail, name='post_detail'), # pylint: disable=no-member
]
