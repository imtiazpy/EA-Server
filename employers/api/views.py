from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .serializers import EmployerUserSerializer

User = get_user_model()


class EmployerUserAPIView(RetrieveUpdateDestroyAPIView):
    """Employer User Profile Retrieve, Update, Delete"""

    serializer_class = EmployerUserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id, is_active=True, type='EMPLOYER')

