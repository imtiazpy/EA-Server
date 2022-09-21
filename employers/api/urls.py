from django.urls import path

from .views import EmployerUserAPIView


app_name = "employers"

urlpatterns = [
    path('profile/', EmployerUserAPIView.as_view(), name='employer-profile'),
]