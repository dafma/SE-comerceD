__author__ = 'seader'
import os
from celery import Celery
from django.conf import settings

#set the default Django settings module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecomiendaYGana.settings')

app = Celery('RecomiendaYGana')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)