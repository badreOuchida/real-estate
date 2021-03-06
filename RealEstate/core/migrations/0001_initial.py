# Generated by Django 3.0.4 on 2021-04-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propreties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=160)),
                ('location', models.CharField(max_length=30)),
                ('chambres', models.CharField(max_length=60)),
                ('air', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('S', 'Sell'), ('R', 'Rent')], max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
