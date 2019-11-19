import os
from celery import Celery

# Переменная окружения, содержащая название файла настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

app = Celery('my_shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

