import os
from this import d
from numpy import datetime_data
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .settings import SENDGRID_API_KEY

# template_id=os.environ.get('TEMPLATE_ID')
# print(template_id,"**************")
def sendgrid_email(recelver,context):
    message = Mail(
        from_email='tushar.citrusbug@gmail.com',
        to_emails=recelver,
    )
    message.dynamic_template_data = context
    message.template_id = 'd-8503ca07141d49f2bb716d9305b1500c'
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        return "done"
