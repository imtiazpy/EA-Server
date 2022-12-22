from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from employers.models import EmployerProfile
from jobseekers.models import JobSeekersProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    If a user is created, and the user is an employer, create an employer profile. If the user is a job seeker, create a job seeker profile
    
    :param sender: The model class
    :param instance: The instance of the model that is being saved
    :param created: A boolean; True if a new record was created
    """
    if created:
        if instance.type == 'EMPLOYER':
            EmployerProfile.objects.create(owner=instance)
        elif instance.type == 'JOB_SEEKER':
            JobSeekersProfile.objects.create(owner=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    If the user is an employer, save the employer profile. If the user is a job seeker, save the job seeker profile
    
    :param sender: The model class
    :param instance: The instance being saved
    """
    if instance.type == 'EMPLOYER':
        instance.employer_profile.save()
    elif instance.type == 'JOB_SEEKER':
        instance.job_seeker_profile.save()