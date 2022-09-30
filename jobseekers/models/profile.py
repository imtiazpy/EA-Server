from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()

class Gender(models.IntegerChoices):
    """Gender choices for job seekers"""
    MAlE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'

class JobSeekersProfile(models.Model):
    """Model for Job seekers profile info"""

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='job_seeker_profile'
    )
    summary = models.TextField(_("Summary"), max_length=255, blank=True, null=True)
    gender = models.IntegerField(_("Gender"), choices=Gender.choices, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=False)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)
    country = models.CharField(_('Country'), max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.id}-{self.owner.get_full_name()}'
