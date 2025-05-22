import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Force Celery to use solo mode on macOS
if os.name == "posix" and "Darwin" in os.uname().sysname:
    app.conf.worker_pool = "solo"

app.autodiscover_tasks()