from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


from assessment.models import Assessment, Result


User = get_user_model()


class AssessmentListSerializer(ModelSerializer):
    """Serializer for Listing Assessment"""

    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'duration', 'created_by', )
        read_only_fields = ('id', )
    

class AssessmentSerializer(ModelSerializer):
    """Serializer for Assessment Create, Detail, update view"""

    class Meta:
        model = Assessment
        fields = ('id', 'type', 'title', 'duration', 'is_published', 'created_by', )
        read_only_fields = ('id', )

    def validate_created_by(self, value):
        """Validating created_by field value whether it's appropriate or not"""
        created_by = User.objects.get(id=value.id)

        if created_by != self.context['request'].user:
            raise serializers.ValidationError("You do not have permission to crete assessment for this user")
        return value 


class ResultSerializer(ModelSerializer):
    """Serializer to list, create Result"""

    class Meta:
        model = Result
        fields = ('id', 'job_seeker', 'assessment', 'marks', 'date' )
        read_only_fields = ('id', )

    def validate_job_seeker(self, value):
        """validating appropriate job_seeker"""

        job_seeker = User.objects.get(id=value.id)

        if job_seeker != self.context['request'].user:
            raise serializers.ValidationError("Invalid Job Seeker")
        return value

    def validate_assessment(self, value):
        """Validating the assessment whether its current users or not"""

        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create result for this assessment")
        return value 