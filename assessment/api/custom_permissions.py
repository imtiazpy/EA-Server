from rest_framework.permissions import BasePermission

class AssessmentWritePermission(BasePermission):
    message = "Only the employers can create Assessments"

    def has_permission(self, request, view):
        """
        If the user is an employer, return True. Otherwise, return False
        
        :param request: The request object
        :param view: the view being accessed
        :return: The user's type.
        """
        return request.user.type == 'EMPLOYER'