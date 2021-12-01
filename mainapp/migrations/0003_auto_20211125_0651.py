# Generated by Django 3.2.9 on 2021-11-25 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_auto_20211125_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9e517e16-c93f-4131-bc66-adfb383dff9f'), unique=True),
        ),
        migrations.CreateModel(
            name='ConnectPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_to_be_followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]