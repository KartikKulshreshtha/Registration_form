# Generated by Django 3.1.6 on 2021-06-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20210605_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='username',
        ),
    ]
