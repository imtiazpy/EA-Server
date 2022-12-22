from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .serializers import JobSeekerUserSerializer

User = get_user_model()


class JobSeekerUserAPIView(RetrieveUpdateDestroyAPIView):
    """Job seeker profile Retrieve, Update, Delete"""
    serializer_class = JobSeekerUserSerializer
    queryset = User.objects.all()

    def get_object(self):
        """
        It returns the user object if the user is active and has the type 'JOB_SEEKER'
        :return: The user object.
        """
        return get_object_or_404(
            User, 
            id=self.request.user.id, 
            is_active=True, 
            type='JOB_SEEKER'
        )