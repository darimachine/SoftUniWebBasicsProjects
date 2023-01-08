from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(
                _('%(value) is not only letter'),
            params={'value': value},
                                  )