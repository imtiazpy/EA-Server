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
        """
        It takes the uid and token from the url, and sends a post request to the activation endpoint with the uid and token as the payload
        
        :param request: The request object
        :param uid: The user's id
        :param token: The token that was sent to the user's email
        :param formant: This is the format of the response. It can be either json or html
        :return: The response is a redirect to the react frontend.
        """
        payload = {'uid': uid, 'token': token}
        url = 'http://127.0.0.1:8000/api/v1/auth/users/activation/'

        response = requests.post(url, data=payload)
        # redirecting to frontend after is successfull
        return redirect('http://localhost:3000/activation-success')