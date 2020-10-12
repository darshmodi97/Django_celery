import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')
app = Celery('celery_django')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {

    'create_file_perioditically':{
        'task': 'celery_app.tasks.create_file',
        'schedule' : crontab(minute= '*/1'),

    }
}
app.autodiscover_tasks()

@app.task(bind =True)
def debug_task(self):
    print('Request : {0!r}'.format(self.request))