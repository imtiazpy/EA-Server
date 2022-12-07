from django.urls import path
from .views import (
    PublicAssessmentListAPIView,
    PublicAssessmentRetrieveAPIView,
    AssessmentCreateAPIView,
    AssessmentListAPIView,
    AssessmentRetrieveUpdateDestroyAPIView,
    ResultListCreateAPIView
)

app_name = 'assessment'

urlpatterns = [
    path('', AssessmentCreateAPIView.as_view(), name='create-assessment'),
    path('assessments/', AssessmentListAPIView.as_view(), name='assessments'),
    path('<int:id>/', AssessmentRetrieveUpdateDestroyAPIView.as_view(), name='update-assessment'),
    path('public/', PublicAssessmentListAPIView.as_view(), name='public-assessments'),
    path('public/<int:id>/', PublicAssessmentRetrieveAPIView.as_view(), name='public-assessment'),
    path('results/', ResultListCreateAPIView.as_view(), name='results'),
]