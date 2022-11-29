"""
    app application URL Configuration.
"""

from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "app"

urlpatterns = [
    path("", views.Create_Account.as_view(), name="index"),
    path(
        "index.html/",
        RedirectView.as_view(pattern_name="app:create_account"),
        name="index_redirect"
    ),
    path("menu/", views.Menu.as_view(), name="menu"),
    path("reward-collection/", views.Reward_Collection.as_view(), name="reward_collection"),
    path("report/", views.Report.as_view(), name="report"),
    path("collect/", views.Collect.as_view(), name="collect"),
    path("leaderboard/", views.Leaderboard.as_view(), name="leaderboard")
]