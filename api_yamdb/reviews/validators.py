from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    if value < 1900 or value > timezone.now().year:
        raise ValidationError(
            '%(value)s is not a correct year!', params={'value': value}
        )
