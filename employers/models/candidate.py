from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InvitedCandidate(models.Model):
    """Job seekers that will be connected with Employers"""
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_candidates')
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Candidate-{self.job_seeker.name}'

    # TODO: The Invited Candidate functionality is incomplete. we will work on it later
    