"""
URL configuration for whiteboard project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("edblog.urls"), name="edblog-urls"),
]

handler404 = 'edblog.views.custom_404'
