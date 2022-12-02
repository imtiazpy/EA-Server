from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from assessment.api.serializers import (
    AssessmentListSerializer, 
    AssessmentSerializer,
    ResultSerializer
)
from assessment.api.custom_permissions import AssessmentWritePermission
from assessment.models import Assessment, Result

User = get_user_model()



class AssessmentPublicListAPIView(ListAPIView):
    """Listing Public Assessments"""
    
    serializer_class = AssessmentListSerializer

    def get_queryset(self):
        if self.request.user.type == 'JOB_SEEKER':
            return Assessment.objects.filter(is_public=True)

class AssessmentCreateAPIView(CreateAPIView):
    """
    View for Creating Assessment. Only The Employer can create Assessment.
    """

    # The permission class checks whether the user is of type EMPLOYER or not
    permission_classes = [AssessmentWritePermission]

    # Assessment__created_by field is being validated in the serializer
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class AssessmentListAPIView(ListAPIView):
    """
    View for listing Assessment in the Employer dashboard
    """
    serializer_class = AssessmentListSerializer
    
    def get_queryset(self):
        return Assessment.objects.filter(created_by=self.request.user)


class AssessmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Assessment Retrieve, Update and Destroy view for the Employer"""

    serializer_class = AssessmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Assessment.objects.filter(created_by=self.request.user)



class ResultListCreateAPIView(ListCreateAPIView):
    """View for Listing and creating Results"""
    
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.filter(job_seeker=self.request.user)
