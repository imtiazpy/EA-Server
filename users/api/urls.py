from django.urls import path

from users.api.views import UserActivationView


app_name = "users"

urlpatterns = [
    path('activate/<str:uid>/<str:token>', UserActivationView.as_view()),
]