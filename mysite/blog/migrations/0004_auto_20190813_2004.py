# Generated by Django 2.2.4 on 2019-08-13 12:04

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_clicks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
