# Generated by Django 3.2.9 on 2021-11-26 05:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211125_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
