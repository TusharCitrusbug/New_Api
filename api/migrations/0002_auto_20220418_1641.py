# Generated by Django 3.1.4 on 2022-04-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='postal_code',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
