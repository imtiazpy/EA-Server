from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404

from employers.models import EmployerProfile

User = get_user_model()


from employers.models import EmployerProfile, InvitedCandidate

class EmployerProfileSerializer(serializers.ModelSerializer):
    """This serializer is used in EmployerUserSerializer"""

    class Meta:
        model = EmployerProfile
        fields = (
            'id',
            'industry_type',
            'hq',
            'company_name',
            'company_size',
            'description',
            'revenue',
            'year_of_form',
        )
        read_only_fields = ('id', )



class EmployerUserSerializer(serializers.ModelSerializer):
    """Retrieve, Update, Delete Employer Profile"""
    employer_profile = EmployerProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('name', 'avatar', 'type', 'employer_profile', )
        read_only_fields = ('id', 'type', )

    @transaction.atomic
    def update(self, instance, validated_data):
        """For updating User and Profile info"""
        ModelClass = self.Meta.model
        employer_profile = validated_data.pop('employer_profile', {})
        # saving the User info. EmployerProfile info extracted with pop
        ModelClass.objects.filter(id=instance.id).update(**validated_data)

        if employer_profile:
            EmployerProfile.objects.filter(owner=instance).update(**employer_profile)

        new_instance = get_object_or_404(ModelClass, id=instance.id)
        return new_instance

    

class InvitedCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedCandidate
        fields = ('id', 'employer', 'job_seeker', )
        read_only_fields = ('id', )
    # TODO: Incompete, We will work on it later