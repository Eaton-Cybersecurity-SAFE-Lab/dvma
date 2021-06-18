from django.http import JsonResponse
from django.shortcuts import render
from .models import DamSensor


# Create your views here.
def getsensorlevels(request):
    sensorjson = [{
        "name": sensor.sensor_name,
        "value": sensor.sensor_value
    } for sensor in DamSensor.objects.all()]
    print(sensorjson)
    return JsonResponse({
        "results": sensorjson
    })
