import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# template_id=os.environ.get('TEMPLATE_ID')
# print(template_id,"**************")
def sendgrid_email(recelver,mail_subject,context):
    message = Mail(
        from_email='tushar.citrusbug@gmail.com',
        to_emails=recelver,
        subject=mail_subject,
    )
    message.dynamic_template_data = context
    message.template_id = 'd-8503ca07141d49f2bb716d9305b1500c'
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        return "done"


