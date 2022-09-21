"""
EAconfig URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


# Admin placeholder change
admin.site.site_header = "Employee Assessment"
admin.site.site_title = "Employee Assessment Admin Panel"
admin.site.index_title = "Employee Assessment Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('employers/', include('employers.api.urls', namespace='employers')),
        path('job-seekers/', include('jobseekers.api.urls', namespace='job-seekers')),
    ])),
]
