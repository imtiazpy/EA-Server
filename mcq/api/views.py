from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from mcq.api.serializers import (
    MultipleChoiceQuestionListSerializer, 
    MultipleChoiceQuestionSerializer
)

from mcq.models import MCQuestion

class MultipleChoiceQuestionListCreateAPIView(ListCreateAPIView):
    """MCQ Listing and create api view"""

    def get_queryset(self):
        return MCQuestion.objects.filter(assessment__created_by = self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MultipleChoiceQuestionSerializer
        return MultipleChoiceQuestionListSerializer