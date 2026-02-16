import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zamar_springs.settings")

app = Celery("zamar_springs")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
