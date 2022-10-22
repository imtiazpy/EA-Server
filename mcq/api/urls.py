from django.urls import path
from .views import (
    MultipleChoiceQuestionListCreateAPIView
)

app_name = 'mcq'

urlpatterns = [
    path('mc-questions/', MultipleChoiceQuestionListCreateAPIView.as_view(), name='mc-questions'),
]