# Generated by Django 3.1.4 on 2022-04-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220419_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
