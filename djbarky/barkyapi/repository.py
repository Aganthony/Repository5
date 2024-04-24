# repository.py
from django.core.exceptions import ObjectDoesNotExist
from .models import Patient, HealthMetric

class PatientRepository:
    @staticmethod
    def get_patient(patient_id):
        try:
            return Patient.objects.get(id=patient_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_patient(name, date_of_birth, medical_history):
        return Patient.objects.create(name=name, date_of_birth=date_of_birth, medical_history=medical_history)

    @staticmethod
    def update_patient(patient_id, **kwargs):
        patient = Patient.objects.get(id=patient_id)
        for key, value in kwargs.items():
            setattr(patient, key, value)
        patient.save()
        return patient

    @staticmethod
    def delete_patient(patient_id):
        patient = Patient.objects.get(id=patient_id)
        patient.delete()

class HealthMetricRepository:
    @staticmethod
    def add_metric_to_patient(patient_id, type, value):
        patient = PatientRepository.get_patient(patient_id)
        if patient:
            return HealthMetric.objects.create(patient=patient, type=type, value=value)
        return None

    @staticmethod
    def get_metrics_for_patient(patient_id):
        return HealthMetric.objects.filter(patient_id=patient_id).order_by('-recorded_at')
