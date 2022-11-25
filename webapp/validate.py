from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.validators import BaseValidator

def at_least_10(string):
    if len(string) < 8:
        raise ValidationError('Korotkoe znachenie')

@deconstructible
class MinLengthValidator(BaseValidator):
    message = '"%(value)s" imeet dlinu %(show_value)d! doljno byt minimum %(limit_value)d simvolov!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)