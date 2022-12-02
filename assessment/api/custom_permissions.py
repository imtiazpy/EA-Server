from rest_framework.permissions import BasePermission

class AssessmentWritePermission(BasePermission):
    message = "Creating Assessment is restricted for the Employers only"

    def has_permission(self, request, view):
        # returns True if the user type is EMPLOYER
        return request.user.type == 'EMPLOYER'