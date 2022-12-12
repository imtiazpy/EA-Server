from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from assessment.api.serializers import (
    PublicAssessmentSerializer,
    PublicAssessmentDetailSerializer,
    AssessmentListSerializer, 
    AssessmentSerializer,
    ResultSerializer
)
from assessment.api.custom_permissions import AssessmentWritePermission
from assessment.models import Assessment, Result

from mcq.api.serializers import MultipleChoiceQuestionSerializer
from mcq.models import MCQuestion

User = get_user_model()

# ===================Public Assessments====================
class PublicAssessmentListAPIView(ListAPIView):
    """
    Listing Public Assessments. 
    Both the Employer and job seekers can view the public assessments
    """
    serializer_class = PublicAssessmentSerializer
    queryset = Assessment.objects.filter(is_public=True)


class PublicAssessmentRetrieveAPIView(RetrieveAPIView):

    serializer_class = PublicAssessmentDetailSerializer
    """
        TODO:somehow we need to determine the type of assessment. Then we will use the serializer of question that matches with the type of assessment. Then we have to filter those questions that are associated with the assessment
    """
    lookup_field = 'id'

    def get_queryset(self):
        return Assessment.objects.filter(is_public=True)



# =================End Public Assessment===================


# ====================Private Assessment================
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

# ===================End Private Assessment==================

class ResultListCreateAPIView(ListCreateAPIView):
    """View for Listing and creating Results"""
    
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.filter(job_seeker=self.request.user)
