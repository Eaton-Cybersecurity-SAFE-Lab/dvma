# Generated by Django 3.1.7 on 2021-04-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DamSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.TextField(max_length=255, verbose_name='Sensor Name')),
                ('sensor_value', models.IntegerField(verbose_name='Sensor Value')),
            ],
        ),
    ]
