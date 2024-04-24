from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.name

class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, related_name='health_metrics', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} for {self.patient.name}: {self.value}"

class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, related_name='treatment_plans', on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Treatment Plan for {self.patient.name} starting on {self.start_date}"
