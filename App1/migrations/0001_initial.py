# Generated by Django 3.2 on 2021-07-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb1',
            fields=[
                ('ID', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Date', models.DateField(default=None)),
                ('Time', models.TimeField(default=None)),
                ('Temperature', models.FloatField(default=None)),
                ('Humidity', models.IntegerField()),
                ('Wind_Speed', models.FloatField(default=None)),
                ('Max_Wind_Gust', models.FloatField(default=None)),
                ('Precipitation', models.FloatField(default=None)),
            ],
            options={
                'db_table': 'Weather_Station',
            },
        ),
        migrations.CreateModel(
            name='tb2',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Date', models.DateField(default=None)),
                ('Time', models.TimeField(default=None)),
                ('Solar_Radiation', models.FloatField(default=None)),
            ],
            options={
                'db_table': 'Pyranometer',
            },
        ),
    ]