from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InvitedCandidate(models.Model):
    """Job seekers that will be connected with Employers"""
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited-candidates')
    job_seeker = models.OneToOneField(User, on_delete=models.CASCADE)
    