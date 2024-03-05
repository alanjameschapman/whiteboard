from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as_view() required for class-based views.
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), # pylint: disable=no-member
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
