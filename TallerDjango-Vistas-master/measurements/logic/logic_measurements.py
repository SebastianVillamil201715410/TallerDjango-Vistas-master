from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements
def get_measurement_id(id: int):
    measurement = Measurement.objects.get(pk=id)
    return measurement
def delete_measurement_id(id: int):
    measurement = Measurement.objects.filter(pk=id).delete()
def update_measuremente_id(id:int, value, unit, place, datetime):
    measurement = Measurement.objects.filter(pk=id).update(value=value, unit=unit, place=place, datetime=datetime)