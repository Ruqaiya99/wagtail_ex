# Generated by Django 2.2.9 on 2020-01-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('flex', '0004_flexpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FlexPage',
        ),
    ]
