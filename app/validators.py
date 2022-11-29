import emoji
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_emoji(value):
    if not emoji.is_emoji(value) and value is not None:
        raise ValidationError(
            _("%(value)s is not an emoji"),
            params={'value': value}
        )