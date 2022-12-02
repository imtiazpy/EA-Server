from django.urls import path
from .views import (
    # AssessmentListCreateAPIView, 
    AssessmentPublicListAPIView,
    AssessmentCreateAPIView,
    AssessmentListAPIView,
    AssessmentRetrieveUpdateDestroyAPIView,
    ResultListCreateAPIView
)

app_name = 'assessment'

urlpatterns = [
    path('', AssessmentCreateAPIView.as_view(), name='create-assessment'),
    path('public/', AssessmentPublicListAPIView.as_view(), name='public-assessments'),
    path('assessments/', AssessmentListAPIView.as_view(), name='assessments'),
    path('<int:id>/', AssessmentRetrieveUpdateDestroyAPIView.as_view(), name='update-assessment'),
    path('results/', ResultListCreateAPIView.as_view(), name='results'),
]