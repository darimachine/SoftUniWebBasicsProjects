from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(
                _('%(value) is not only letter'),
            params={'value': value},
                                  )

def file_max_size_inMB_validator(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize>max_size*1024*1024:
            raise ValidationError(f"Max file size is {max_size}MB")
    return validate
