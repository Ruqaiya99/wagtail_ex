# Generated by Django 2.2.9 on 2020-01-30 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_auto_20200129_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopdetailpage',
            name='content',
        ),
    ]
