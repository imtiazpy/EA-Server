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
        fields = ('id', 'title', 'type', 'duration', )
        read_only_fields = ('id', )



class PublicAssessmentDetailSerializer(ModelSerializer):

    mcq = MultipleChoiceQuestionSerializer(source='mc_questions', many=True)
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'duration', 'mcq', )
        read_only_fields = ('id', )



# ===============End Public Assessment serializers=====================


# This class is a serializer for listing Assessment
class AssessmentListSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'type', 'duration', 'created_by', )
        read_only_fields = ('id', )
    

# The AssessmentSerializer class is a subclass of ModelSerializer. It has a Meta class which specifies
# the model to be used for serialization and the fields to be serialized. The read_only_fields
# attribute specifies the fields that can only be read and not written to. The validate_created_by
# method validates the created_by field value
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