# Generated by Django 3.0.4 on 2021-04-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210424_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
