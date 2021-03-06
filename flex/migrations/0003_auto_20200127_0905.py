# Generated by Django 2.2.9 on 2020-01-27 09:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flex_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flex_page',
            name='contents',
            field=wagtail.core.fields.StreamField([('doc', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('doc_upload', wagtail.documents.blocks.DocumentChooserBlock(required=True))])))]))], blank=True, null=True),
        ),
    ]
