from django.urls import path
from .views import (
    AssessmentListCreateAPIView, 
    AssessmentRetrieveUpdateDestroyAPIView,
)

app_name = 'assessment'

urlpatterns = [
    path('assessments/', AssessmentListCreateAPIView.as_view(), name='assessment'),
    path('assessment/<int:id>/', AssessmentRetrieveUpdateDestroyAPIView.as_view(), name='assessment'),
]