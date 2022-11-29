from django.forms import CharField, TextInput
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.core.validators import RegexValidator

from .models import Profile


class UserCreationForm(BaseUserCreationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                "class": "text-center fs-5 form-control px-3",
                "placeholder": "Display Name"
            }
        ),
        validators=[RegexValidator(r"^(?=(?:.*[A-Za-z].*){2})[A-Z a-z0-9]+$")],
        max_length=10
    )

    class Meta:
        model = Profile
        fields = [
            "username",
            "password1",
            "password2",
            "phone_number",
            "longitude",
            "latitude",
            "radius"
        ]