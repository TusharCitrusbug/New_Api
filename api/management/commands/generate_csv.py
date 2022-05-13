from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from datetime import date
import csv
import boto3
from api.models import *
print(settings.AWS_STORAGE_BUCKET_NAME)
print(settings.AWS_ACCESS_KEY_ID)
print(settings.AWS_SECRET_ACCESS_KEY)
s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                      region_name=settings.AWS_S3_REGION_NAME)

s3_bucket_name=settings.AWS_STORAGE_BUCKET_NAME
class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('input_date', type=str, help='Please enter Date. Formate should be DD/MM/YY')

    def handle(self, *args, **kwargs):
        input_date = kwargs['input_date']
        date_obj = datetime.strptime(input_date, '%d/%m/%y').date()
        
        if input_date:
            plan_list=Plan.objects.filter(plan_datetime__date__range=[date_obj,date.today()])
            if plan_list.exists():

                file_name=f'planes_list{date_obj}.csv'
                file_path=f"{settings.MEDIA_ROOT}\{file_name}"
                with open(file_path,"w") as c:
                    writer = csv.writer(c)
                    writer.writerow(['id',"title", "user", "description", "plan_datetime", "city","postal_code","plan_image","category","is_active"])
                    for _ in plan_list:
                        writer.writerow([_.id, _.title,_.user.username, _.description, _.plan_datetime, _.city.city_name,_.postal_code,_.plan_image,_.category.category_name,_.is_active])
                    # s3.upload_fileobj(c, s3_bucket_name,)
                    s3.upload_file(c.name, s3_bucket_name, file_name)
                    print("39873vvvvvvvvvvvvvvvvvvv949348")
            else:
                print("result not found for what you need")
            # get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

            # objs = s3.list_objects_v2(Bucket='my_bucket')['Contents']
            # last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
            # print(last_added,"348934")
            
            # csv_file=CSV_STORE.objects.create(csv_file=f'media/{file_name}')
            # csv_file.save()
            # os.system('python manage.py collectstatic --noinput')
            # s3.meta.client.upload_file(
            # Filename=file_path,
            # Bucket=s3_bucket_name,
            # Key=file_name)

            # # bucket_location = boto3.client('s3').get_bucket_location(Bucket=s3_bucket_name)
            # # object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            # # bucket_location[settings.AWS_S3_REGION_NAME],
            # # s3_bucket_name,
            # # file_name)
            # # print(object_url,"59454895489548948954895489548954549854894589548954")
            # print(s3,"59454895489548948954895489548954549854894589548954")
            
    
       