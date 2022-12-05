from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from employers.models import InvitedCandidate

from .serializers import EmployerUserSerializer, InvitedCandidateSerializer


User = get_user_model()


class EmployerUserAPIView(RetrieveUpdateDestroyAPIView):
    """Employer User Profile Retrieve, Update, Delete"""

    serializer_class = EmployerUserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id, is_active=True, type='EMPLOYER')


class InvitedCandidateListCreateAPIView(ListCreateAPIView):

    serializer_class = InvitedCandidateSerializer
    queryset = InvitedCandidate.objects.all()
    # TODO: Incomplete, We will work on it later