from re import I
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from api.helper import *

import datetime

from api.models import *

@shared_task(bind=True)
def send_email(self,data):
    
    event_title=data['title']
    plan_datetime=data['plan_datetime']
    description=data['description']
    category=Category.objects.get(id=data['category']).category_name
    mail_subject=f"Invitation for new event: {event_title}"
    for i in User.objects.all():
        context= {
            "event_title":event_title,
            "plan_datetime":plan_datetime,
            "description":description,
            "category":category,
            "user_name":i.username,
            "subject":mail_subject,
        }
        print(context)
        sendgrid_email(i.email,context)
    return data
   
    
@shared_task(bind=True)
def check_plan_date_time(self):
    all_planes=Plan.objects.all()
    for i in all_planes:
        if i.plan_datetime.date() < datetime.datetime.now().date():
            i.is_active=False
            i.save()
        elif i.plan_datetime.date() == datetime.datetime.now().date():
            if  i.plan_datetime.time() < datetime.datetime.now().time():
                i.is_active=False
                i.save()
        else:
            print("it is time travel lol...........")
    
    return f"deleted products at {datetime.datetime.now()}"