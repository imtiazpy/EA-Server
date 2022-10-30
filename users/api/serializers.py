from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """
    Serializer for creating user and retrieving from djoser. 
    we haven't written any view for this. This serializer is referenced in settings.py
    """
    class Meta:
        model = User
        fields = ('id', 'type', 'name', 'email', 'password')



class AvatarUploadSerializer(ModelSerializer):
    # Serializer for only avatar upload
    class Meta:
        model = User
        fields = ('avatar', )