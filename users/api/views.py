from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
import requests

from users.api.serializers import AvatarUploadSerializer


User = get_user_model()

class AvatarUploadView(generics.UpdateAPIView):
    """single endpoint to update the Avatar"""

    serializer_class = AvatarUploadSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id, is_active=True)

class UserActivationView(generics.GenericAPIView):
    """View to activate account upon clicking on the link from activation email"""

    permission_classes = [AllowAny]

    def get(self, request, uid, token, formant=None):
        payload = {'uid': uid, 'token': token}
        url = 'http://127.0.0.1:8000/api/v1/auth/users/activation/'

        response = requests.post(url, data=payload)
        
        return redirect('http://localhost:3000/activation-success')