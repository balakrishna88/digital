# Generated by Django 4.1.2 on 2022-10-30 07:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_alter_blogsapplications_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsapplications',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
