# Generated by Django 3.1.4 on 2022-04-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220418_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
    ]
