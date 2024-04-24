# orm.py
from .models import Patient, HealthMetric

def get_patient_by_id(patient_id):
    return Patient.objects.get(id=patient_id)

def get_all_health_metrics_for_patient(patient_id):
    return HealthMetric.objects.filter(patient_id=patient_id).order_by('-recorded_at')
