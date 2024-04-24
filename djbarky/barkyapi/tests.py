from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Patient, HealthMetric
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    """This class defines the test suite for the Patient model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.patient_name = "John Doe"
        self.patient_dob = "2000-01-01"
        self.patient_medical_history = "No known allergies."
        self.patient = Patient(name=self.patient_name, date_of_birth=self.patient_dob, medical_history=self.patient_medical_history)

    def test_model_can_create_a_patient(self):
        """Test the Patient model can create a patient."""
        old_count = Patient.objects.count()
        self.patient.save()
        new_count = Patient.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.patient_data = {'name': 'Jane Doe', 'date_of_birth': '1990-01-01', 'medical_history': 'Diabetic'}
        self.response = self.client.post(
            reverse('create'),
            self.patient_data,
            format="json")

    def test_api_can_create_a_patient(self):
        """Test the api has patient creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

# Tests for HealthMetric model and API views would be similarly structured

class HealthMetricModelTestCase(TestCase):
    """This class defines the test suite for the HealthMetric model."""
    
    def setUp(self):
        """Define the test client and other test variables."""
        self.patient = Patient.objects.create(name='John Doe', date_of_birth='2000-01-01', medical_history='No known allergies.')
        self.health_metric_type = "Heart Rate"
        self.health_metric_value = 72
        self.health_metric = HealthMetric(patient=self.patient, type=self.health_metric_type, value=self.health_metric_value)

    def test_model_can_create_a_health_metric(self):
        """Test the HealthMetric model can create a health metric."""
        old_count = HealthMetric.objects.count()
        self.health_metric.save()
        new_count = HealthMetric.objects.count()
        self.assertNotEqual(old_count, new_count)


