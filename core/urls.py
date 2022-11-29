"""
    core URL Configuration.
"""

from django.urls import include, path
from django.views.generic.base import RedirectView
from app.admin import site

urlpatterns = [
    path('admin/', site.urls, name="admin"),
    path("", include("app.urls")),
    path("", RedirectView.as_view(pattern_name="app:login"), name="default")
]