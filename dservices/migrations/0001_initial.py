# Generated by Django 4.1.1 on 2022-10-27 19:45

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDServices',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('slug_nameDServices', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogsDServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('pub_date', models.DateField(auto_now=True)),
                ('sub_category', models.CharField(blank=True, max_length=100)),
                ('slug_postDServices', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('img', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dservices.categorydservices')),
            ],
        ),
    ]
