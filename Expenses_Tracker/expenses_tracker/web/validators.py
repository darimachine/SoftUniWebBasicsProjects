from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def OnlyLettersValidator(value):
    for character in value:
        if not character.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxFileSizeValidator:
    def __init__(self,max_file_size):
        self.max_file_size = max_file_size
    def __call__(self,value, *args, **kwargs):
        filesize = value.file.size
        if filesize > self.max_file_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {round(self.max_file_size,2)}')

