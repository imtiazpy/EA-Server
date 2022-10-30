"""
EAconfig URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import IsAuthenticated

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Admin placeholder change
admin.site.site_header = "Employee Assessment"
admin.site.site_title = "Employee Assessment Admin Panel"
admin.site.index_title = "Employee Assessment Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('users/', include('users.api.urls', namespace='users')),
        path('employers/', include('employers.api.urls', namespace='employers')),
        path('job-seekers/', include('jobseekers.api.urls', namespace='job-seekers')),
        path('assessment/', include('assessment.api.urls', namespace='assessment')),
        path('mcq/', include('mcq.api.urls', namespace='mcq')),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


API_INFO = openapi.Info(
    title = "Employee Assessment API",
    default_version = "v1",
    description = "API documentation for Employee Assessment App"
)

API_DOCS_SCHEMA_VIEWS = get_schema_view(
    API_INFO,
    public = True,
    permission_classes = (IsAuthenticated, ),
)

urlpatterns += [
    path("api-docs/", API_DOCS_SCHEMA_VIEWS.with_ui("swagger", cache_timeout=0), name="api_playground")
]