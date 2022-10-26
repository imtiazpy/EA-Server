from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


from assessment.models import Assessment


User = get_user_model()


class AssessmentListSerializer(ModelSerializer):
    """Serializer for Listing Assessment"""

    class Meta:
        model = Assessment
        fields = ('id', 'title', 'duration', 'questions', 'created_by', )
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