from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

@deconstructible
class DuplicateValidator(object):
    message = _('The value is already in the ArrayField.')
    code = 'duplicate'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if len(value) != len(set(value)):
            raise ValidationError(self.message, code=self.code)
