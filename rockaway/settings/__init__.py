from .base import *

try:
    from .local import *
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured('No local settings file found.')
