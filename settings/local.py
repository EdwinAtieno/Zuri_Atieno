from .Atieno import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'twoscoops',
'HOST': 'localhost',
}
}

"""NOT CORRECT FORMAT"""
INSTALLED_APPS += ['eddy', ]