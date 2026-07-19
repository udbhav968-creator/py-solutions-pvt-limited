from django.db import models
from django.conf import settings
from apps.content.models import Doctor
from apps.administration.models import TimeStampedModel

class Appointment(TimeStampedModel):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField(db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', db_index=True)
    symptoms = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appt: {self.user.username} - {self.status}"
