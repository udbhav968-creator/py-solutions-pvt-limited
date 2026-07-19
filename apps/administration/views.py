from rest_framework.views import APIView
from rest_framework.response import Response
from apps.authentication.models import User
from apps.appointments.models import Appointment
from apps.content.models import Doctor, Service

class AdminDashboardView(APIView):
    def get(self, request):
        total_users = User.objects.count()
        total_doctors = Doctor.objects.count()
        total_appointments = Appointment.objects.count()
        pending_appointments = Appointment.objects.filter(status='Pending').count()
        total_services = Service.objects.count()

        data = {
            "statistics": {
                "total_users": total_users,
                "total_doctors": total_doctors,
                "total_appointments": total_appointments,
                "pending_appointments": pending_appointments,
                "total_services": total_services,
            }
        }
        return Response(data)
