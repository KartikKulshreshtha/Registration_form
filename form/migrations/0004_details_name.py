# Generated by Django 3.1.6 on 2021-06-05 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_remove_details_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]