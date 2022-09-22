from django.urls import path
from .views import JobSeekerUserAPIView

app_name = "jobseekers"

urlpatterns = [
    path('profile/', JobSeekerUserAPIView.as_view(), name='job-seeker-profile'),
]