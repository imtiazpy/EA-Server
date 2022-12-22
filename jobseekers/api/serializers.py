from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404

from jobseekers.models import JobSeekersProfile

User = get_user_model()


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    """The serializer is used in JobSeekerUserSerializer"""

    class Meta:
        model = JobSeekersProfile
        fields = (
            'id',
            'summary',
            'gender',
            'date_of_birth',
            'city',
            'country',
        )
        read_only_fields = ('id', )



class JobSeekerUserSerializer(serializers.ModelSerializer):
    """Retrieve, Update, Delete Job Seeker Profile"""
    job_seeker_profile = JobSeekerProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('name', 'avatar', 'type', 'job_seeker_profile', )
        read_only_fields = ('id', 'type', )

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        We are updating the User model with the validated_data, and then we are updating the
        JobSeekersProfile model with the job_seeker_profile data
        
        :param instance: The instance of the model that is being updated
        :param validated_data: This is the data that has been validated by the serializer
        :return: The new instance of the model class
        """
        ModelClass = self.Meta.model
        job_seeker_profile = validated_data.pop('job_seeker_profile', {})
        # saving the User info. job seeker profile is extracted with pop
        ModelClass.objects.filter(id=instance.id).update(**validated_data)

        if job_seeker_profile:
            JobSeekersProfile.objects.filter(owner=instance).update(**job_seeker_profile)
        
        new_instance = get_object_or_404(ModelClass, id=instance.id)
        return new_instance