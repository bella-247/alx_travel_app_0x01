import os
from celery import Celery
from django.conf import settings
import environ

env = environ.Env()
environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

app = Celery("alx_travel_app")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()

# broker from env
app.conf.broker_url = env("CELERY_BROKER_URL", default='amqp://guest:guest@rabbitmq:5672//')