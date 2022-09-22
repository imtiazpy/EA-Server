from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from employers.models import EmployerProfile
from jobseekers.models import JobSeekersProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create profile upon user registration"""

    if created:
        if instance.type == 'EMPLOYER':
            EmployerProfile.objects.create(owner=instance)
        elif instance.type == 'JOB_SEEKER':
            JobSeekersProfile.objects.create(owner=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.type == 'EMPLOYER':
        instance.employer_profile.save()
    elif instance.type == 'JOB_SEEKER':
        instance.job_seeker_profile.save()