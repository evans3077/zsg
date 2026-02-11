import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zamar_springs.settings")

# Render may default to `gunicorn app:app` if no explicit start command is set.
app = get_wsgi_application()
application = app
