# Generated by Django 3.0.4 on 2021-04-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_owners_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owners',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='owners',
            name='printest',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='owners',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
