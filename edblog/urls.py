from django.urls import path
from . import views
from .views import PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as_view() required for class-based views.
    path('create-post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), # pylint: disable=no-member
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
#     path('<slug:slug>/comment_approve/<int:comment_id>/',
#          views.comment_approve, name='comment_approve'),
]
