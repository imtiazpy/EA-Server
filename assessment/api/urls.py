from django.urls import path
from .views import (
    AssessmentListCreateAPIView, 
    AssessmentPublicListAPIView,
    AssessmentRetrieveUpdateDestroyAPIView,
)

app_name = 'assessment'

urlpatterns = [
    path('public-assessments/', AssessmentPublicListAPIView.as_view(), name='public-assessments'),
    path('assessments/', AssessmentListCreateAPIView.as_view(), name='assessments'),
    path('assessment/<int:id>/', AssessmentRetrieveUpdateDestroyAPIView.as_view(), name='assessment'),
]