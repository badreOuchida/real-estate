# Generated by Django 3.0.4 on 2021-04-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210417_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owners',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='propreties',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
