from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from assessment.models import Assessment
from mcq.models import MCQuestion




class MultipleChoiceQuestionListSerializer(ModelSerializer):
    """MCQuestion Listing serializer"""

    class Meta:
        model = MCQuestion
        fields = ('id', 'content', 'assessment', )
        read_only_fields = ('id', )


class MultipleChoiceQuestionSerializer(ModelSerializer):
    """MCQ Detail, Update, Destroy"""

    class Meta:
        model = MCQuestion
        fields = ('id', 'content', 'topic', 'assessment', )
        read_only_fields = ('id', )

    def validate_assessment(self, value):
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create question fro this assessment")
        return value 