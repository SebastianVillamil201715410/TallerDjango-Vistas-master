from django.shortcuts import render

# Create your views here.
from .logic.logic_measurements import get_all_measurements, get_measurement_id, delete_measurement_id, update_measuremente_id
from django.http import HttpResponse, HttpRequest
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')
def get_measurement_id(request,id):
    measurement = get_measurement_id(id)
    measurement_list = serializers.serialize('json', measurement)
    return HttpResponse(measurement_list, content_type='application/json')
def delete_measurement_id(request,id):
    measurement = delete_measurement_id(id)
    return HttpResponse('El elemento {} fue borrado'.format(measurement))
def update_measurement_id(request,id):
    measurement = update_measurement_id(id)