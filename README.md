# Django_celery

In this repository I have provided just simple task which occures periodically by using module Django-celery.
I have written the code for creating text file  which says the time at every 10 seconds.

All the requirements are provided in requirements.txt

- celery configuration is in celery_django/settings.py 
- other configurations is provided in celery_django/celery.py

# celery_app/tasks.py 

In this file we can call add () function from the shell in the terminal using 
python manage.py shell

We can call this function by 2 ways .. 
- ansynchronous calling : add.delay()
- synchronous calling : add()

........ for all the task ......

Here we have to run two commands in two different terminal windows 
1. for redis worker
- celery -A celery_django worker -l INFO

2. for beat 
- celery -A celery_django beat -l INFO
