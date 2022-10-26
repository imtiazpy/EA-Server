from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone

from .enum_helper import JobType, JobCategory
from employers.models import EmployerProfile
from jobseekers.models import JobSeekersProfile


User = get_user_model()


class Job(models.Model):
    """Model for Job"""

    title = models.CharField(
        _('Title'),
        max_length = 100,
        blank = False,
        null = False,
        help_text = _('Title of the Job')
    )
    description = models.TextField(
        _('Description'),
        max_length = 1500,
        blank = False,
        null = False,
        help_text = _('Job Description')
    )
    location = models.CharField(_('Job Location'), max_length=150)
    type = models.IntegerField(_('Job Type'),choices=JobType.choices)
    category = models.CharField(_('Job Category'),max_length=100, choices=JobCategory.choices)
    company_name = models.CharField(_('Company Name'), max_length=100)
    last_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    create_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='jobs',
        verbose_name = _('Created By')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')




class Application(models.Model):
    """model for Applications"""

    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    applicant = models.ForeignKey(JobSeekersProfile, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to='resumes/', null=True, blank=True)
    apply_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
    

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

