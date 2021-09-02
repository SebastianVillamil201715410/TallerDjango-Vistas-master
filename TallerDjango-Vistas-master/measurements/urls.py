from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('get/<int:id>', views.get_measurement_id, name='measurementId'),
    path('delete/<int:id>', views.delete_measurement_id(), name='measurementId'),
    path('update/<int:id>', views.update_measurement_id(), name='measurementId'),
]