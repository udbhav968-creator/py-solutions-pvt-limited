from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.authentication.models import User
from apps.appointments.models import Appointment
from apps.content.models import Doctor, Service
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AdminDashboardView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    
    @method_decorator(cache_page(60 * 5)) # Cache for 5 minutes
    def get(self, request):
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)

        # Advanced Aggregation & Analytics
        stats = Appointment.objects.aggregate(
            total_appointments=Count('id'),
            pending_appointments=Count('id', filter=Q(status='Pending')),
            recent_appointments=Count('id', filter=Q(created_at__gte=thirty_days_ago))
        )

        data = {
            "success": True,
            "statistics": {
                "users": {
                    "total": User.objects.count(),
                    "doctors": Doctor.objects.filter(is_deleted=False).count()
                },
                "appointments": {
                    "total": stats['total_appointments'],
                    "pending": stats['pending_appointments'],
                    "last_30_days": stats['recent_appointments']
                },
                "services": Service.objects.filter(is_deleted=False).count()
            }
        }
        return Response(data)
