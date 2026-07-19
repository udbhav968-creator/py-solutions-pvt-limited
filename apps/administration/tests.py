from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.authentication.models import User
from apps.appointments.models import Appointment
from apps.content.models import Doctor, Service

class AdminDashboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('admin-dashboard')
        
        # Create dummy data
        self.user = User.objects.create(username='testuser', email='test@test.com')
        self.doctor = Doctor.objects.create(
            first_name='John', last_name='Doe', specialization='General',
            email='doctor@test.com', phone='1234567890'
        )
        self.service = Service.objects.create(title='Consultation', description='Basic checkup')
        self.appointment = Appointment.objects.create(
            user=self.user, doctor=self.doctor, appointment_date='2026-07-20T10:00:00Z', status='Pending'
        )

    def test_admin_dashboard_stats(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.data.get('statistics')
        self.assertIsNotNone(data)
        self.assertEqual(data['total_users'], 1)
        self.assertEqual(data['total_doctors'], 1)
        self.assertEqual(data['total_services'], 1)
        self.assertEqual(data['total_appointments'], 1)
        self.assertEqual(data['pending_appointments'], 1)
