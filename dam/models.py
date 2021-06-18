from django.db import models


# Create your models here.

class DamSensor(models.Model):
    sensor_name = models.TextField(verbose_name="Sensor Name", max_length=255)
    sensor_value = models.IntegerField(verbose_name="Sensor Value")

    def __str__(self):
        return f"{self.sensor_name}:{self.sensor_value}"
