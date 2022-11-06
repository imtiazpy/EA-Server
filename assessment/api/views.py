from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from assessment.api.serializers import (
    AssessmentListSerializer, 
    AssessmentSerializer,
)
from assessment.models import Assessment

User = get_user_model()



class AssessmentPublicListAPIView(ListAPIView):
    """Listing Public Assessments"""
    
    serializer_class = AssessmentListSerializer

    def get_queryset(self):
        if self.request.user.type == 'JOB_SEEKER':
            return Assessment.objects.filter(is_public=True)
    

class AssessmentListCreateAPIView(ListCreateAPIView):
    """View for listing and creating the Assessment"""

    def get_queryset(self):
        return Assessment.objects.filter(created_by=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AssessmentSerializer
        return AssessmentListSerializer
    
    def perform_create(self, serializer):
        serializer.save()


class AssessmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Assessment Retrieve, Update and Destroy"""

    serializer_class = AssessmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Assessment.objects.filter(created_by=self.request.user)
