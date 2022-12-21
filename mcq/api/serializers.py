from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from assessment.models import Assessment
from mcq.models import MCQuestion, Choice



class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'content', 'is_correct', )
        read_only_fields = ('id', )

class MultipleChoiceQuestionListSerializer(ModelSerializer):
    """MCQuestion Listing serializer"""

    class Meta:
        model = MCQuestion
        fields = ('id', 'content', 'assessment', )
        read_only_fields = ('id', )


class MultipleChoiceQuestionSerializer(ModelSerializer):
    """MCQ Detail, Update, Destroy"""

    choices = ChoiceSerializer(many=True)

    class Meta:
        model = MCQuestion
        fields = ('id', 'content', 'topic', 'assessment', 'choices', )
        read_only_fields = ('id', )

    def validate_assessment(self, value):
        """
        If the assessment is not created by the user, raise a validation error
        
        :param value: The value that is being validated
        :return: The value of the assessment
        """
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create question for this assessment")
        return value 