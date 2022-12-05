from django.urls import path

from .views import EmployerUserAPIView, InvitedCandidateListCreateAPIView


app_name = "employers"

urlpatterns = [
    path('profile/', EmployerUserAPIView.as_view(), name='employer-profile'),
    # path('candidates/', InvitedCandidateListCreateAPIView.as_view(), name='candidates'),
]