# command to start celery

# elery -A <project_name.celery> worker -l info


from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from pytz import timezone
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','plan_module.settings')  
app =Celery('plan_module')
app.conf.enable_utc =False

app.conf.update(timezone ='Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    "deactivate-expired-planes":{
        'task':'api.task.check_plan_date_time',
        'schedule':60
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')