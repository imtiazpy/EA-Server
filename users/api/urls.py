from django.urls import path

from users.api.views import UserActivationView, AvatarUploadView


app_name = "users"

urlpatterns = [
    path('avatar-upload/', AvatarUploadView.as_view(), name='avatar-upload'),
    path('activate/<str:uid>/<str:token>', UserActivationView.as_view()),
]