from __future__ import absolute_import,unicode_literals
from celery.decorators import task
from celery.decorators import periodic_task
import time
from datetime import datetime
from celery.schedules import crontab
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name='add_two_number')# this is task name while calling worker(redis...)
def add(a,b):
    # time.sleep(10)
    return a + b

# @periodic_task(run_every = (crontab(minute='*/1')),name='create_file',ignore_result=True)

@task()
def create_file():
    file = open('/home/<your username>/test.txt','a')
    file.write("\n hello darsh the time is :" +str(datetime.now()))
    file.close()
    logger.info("File will be created in just minute")
    