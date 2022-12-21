from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


from assessment.models import Assessment, Result
from mcq.api.serializers import MultipleChoiceQuestionSerializer


User = get_user_model()

# =====================Public Assessment serializers==================

class PublicAssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'duration', 'slug', )
        read_only_fields = ('id', 'slug', )



class PublicAssessmentDetailSerializer(ModelSerializer):

    mc_questions = MultipleChoiceQuestionSerializer(many=True)
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'duration', 'slug', 'mc_questions', )
        read_only_fields = ('id', 'slug', )



# ===============End Public Assessment serializers=====================


class AssessmentListSerializer(ModelSerializer):
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
        """
        It validates the value of the created_by field, and if the value is not the same as the user who
        is making the request, it raises a serializer validation error
        
        :param value: The value of the field being validated
        :return: The value of the field being validated.
        """
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
        """
        It checks if the job seeker is the same as the user who is logged in
        
        :param value: The value that is being validated
        :return: The validated value is being returned.
        """
        job_seeker = User.objects.get(id=value.id)

        if job_seeker != self.context['request'].user:
            raise serializers.ValidationError("Invalid Job Seeker")
        return value

    def validate_assessment(self, value):
        """
        It validates the assessment whether its current users or not
        
        :param value: The value that is being validated
        :return: The assessment object is being returned.
        """
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create result for this assessment")
        return value 