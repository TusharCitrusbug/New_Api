# Generated by Django 3.1.4 on 2022-04-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('category_image', models.ImageField(default='default.jpg', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_datetime', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('postal_code', models.PositiveIntegerField()),
                ('plan_image', models.ImageField(default='default.jpg', upload_to='media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]