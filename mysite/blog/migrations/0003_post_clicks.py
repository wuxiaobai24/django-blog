# Generated by Django 2.2.4 on 2019-08-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190810_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
