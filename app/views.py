"""
    Webpage views in app application.
"""

from django.contrib.auth.models import User as BaseUser
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import F
from random import choice as random_choice

from .forms import UserCreationForm
from .models import Profile

class Create_Account(CreateView):
    template_name = "app/create_account.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        """ Redirects successful join to waiting room. """

        base_user = BaseUser.objects.create_user(
            form.cleaned_data["username"],
            password=form.cleaned_data["password1"]
        )
        login(self.request, base_user)

        Profile.objects.create(
            _base_user=base_user,
            phone_number=form.cleaned_data["phone_number"],
            longitude=form.cleaned_data["longitude"],
            latitude=form.cleaned_data["latitude"],
            radius=form.cleaned_data["radius"]
        )

        return redirect("app:menu")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )

class Menu(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "app/menu.html"

class Report(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "app/report.html"

class Collect(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "app/collect.html"

class Reward_Collection(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "app/reward_collection.html"

    def get_context_data(self, **kwargs):
        userQS = Profile.objects.filter(id=self.request.user.profile.id)
        userQS.update(points=F("points") + self.request.GET["points"])

        prize = random_choice(["No Prize", "+5 Duck Points", "+10 Duck Points", "+25 Duck Points", "Free Colour Change"])
        if prize == "+5 Duck Points":
            userQS.update(points=F("points") + 5)
        elif prize == "+10 Duck Points":
            userQS.update(points=F("points") + 10)
        elif prize == "+25 Duck Points":
            userQS.update(points=F("points") + 25)

        user = userQS.get()
        user.refresh_from_db()

        if user.points >= 150:
            user.rank = user.DIAMOND
            user.save()
        elif user.points >= 100:
            user.rank = user.GOLD
            user.save()
        elif user.points >= 70:
            user.rank = user.SILVER
            user.save()
        elif user.points >= 40:
            user.rank = user.BRONZE
            user.save()


        user.refresh_from_db()

        context = super().get_context_data()
        context["prize"] = prize
        context["new_points"] = self.request.GET["points"]
        context["user_updated"] = user

        return context

    def post(self, request, *args, **kwargs):
        if request.POST["shop"] == "colour":
            self.request.user.profile.colour = request.POST["colour"]
            self.request.user.profile.save()

            userQS = Profile.objects.filter(id=self.request.user.profile.id)
            userQS.update(points=F("points") - 25)
        elif request.POST["shop"] == "emoji":
            self.request.user.profile.emoji = request.POST["emoji"]
            self.request.user.profile.save()

            userQS = Profile.objects.filter(id=self.request.user.profile.id)
            userQS.update(points=F("points") - 50)

        return redirect("app:menu")

class Leaderboard(TemplateView):
    template_name = "app/leaderboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context.update({
            "gooducks": Profile.objects.order_by("-points", "rank", "_base_user__username")[:5],
            "baducks": Profile.objects.order_by("points", "rank", "_base_user__username")[:5],
            "wallofshame": Profile.objects.filter(_added_to_wall__gt=timezone.now()-timedelta(minutes=30))[:5]
        })

        return context