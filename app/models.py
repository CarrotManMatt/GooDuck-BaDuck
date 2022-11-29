"""
    Model objects in app application.
"""

from django.contrib.auth.models import User as BaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField
from datetime import timedelta

from .validators import validate_emoji


class Profile(models.Model):
    USERNAME_FIELD = "_base_user__username"

    DIAMOND = "DI"
    GOLD = "GO"
    SILVER = "SI"
    BRONZE = "BR"
    UNRANKED = "UR"
    rank_choices = [
        (DIAMOND, "Diamond"),
        (GOLD, "Gold"),
        (SILVER, "Silver"),
        (BRONZE, "Bronze"),
        (UNRANKED, "Unranked")
    ]

    _base_user = models.OneToOneField(
        BaseUser,
        on_delete=models.CASCADE,
        verbose_name="Base User"
    )
    phone_number = PhoneNumberField("Phone Number")
    longitude = models.DecimalField(
        "Search Point Longitude",
        max_digits=19,
        decimal_places=16
    )
    latitude = models.DecimalField(
        "Search Point Latitude",
        max_digits=19,
        decimal_places=16
    )
    radius = models.SmallIntegerField(
        "Search Point Radius",
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )
    colour = ColorField(
        "Username Colour",
        default="#000000"
    )
    rank = models.CharField(
        "Rank",
        max_length=2,
        choices=rank_choices,
        default=UNRANKED
    )
    points = models.IntegerField(
        "Duck Points",
        default=0
    )
    emoji = models.CharField(
        "Custom Emoji",
        max_length=7,
        blank=True,
        null=True,
        validators=[validate_emoji]
    )
    _added_to_wall = models.DateTimeField(
        "Last time added to wall",
        default=timezone.now() - timedelta(minutes=50)
    )

    @property
    def base_user(self):
        return self._base_user

    @property
    def added_to_wall(self):
        return self._added_to_wall

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        output = "@" + self.base_user.username
        if self.emoji is not None:
            output += "&nbsp&nbsp&nbsp&nbsp" + self.emoji
        return mark_safe(output)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Report(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    _completed = models.BooleanField(default=False)

    @property
    def completed(self):
        """ Locked/private value of _completed. """

        return self._completed

    class Meta:
        verbose_name = "Fly Tipping Report"

    def __str__(self):
        if self.completed is True:
            return "Completed Fly Tipping Report"
        else:
            return f"Long: {self.longitude}, Lat:{self.latitude} - Reported by {self.user}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)