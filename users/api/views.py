from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
import requests




class UserActivationView(generics.GenericAPIView):
    """View to activate account upon clicking on the link from activation email"""

    permission_classes = [AllowAny]

    def get(self, request, uid, token, formant=None):
        payload = {'uid': uid, 'token': token}
        url = 'http://127.0.0.1:8000/api/v1/auth/users/activation/'

        response = requests.post(url, data=payload)
        
        return redirect('http://localhost:3000/activation-success')