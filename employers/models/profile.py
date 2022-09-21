from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


User = get_user_model()

class IndustryType(models.TextChoices):
    """Employer will add their company type from enum"""
    IT = "IT", "Information Technology"
    INTERNET = "INTERNET", "Internet"
    SOFTWARE = "SOFTWARE", "Software"

class Size_Choices(models.TextChoices):
    "Company size choices to be selected by the employer"
    micro = "1-9", "1-9"
    small = "10-49", "10-49"
    medium = "50-249", "50-249"


class EmployerProfile(models.Model):
    """
    Model for Employer Profile info
    """
    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='employer_profile'
    )
    industry_type = models.CharField(
        _("Employer Type"),
        max_length=70,
        choices=IndustryType.choices,
        null=True,
        blank=True
    ) 
    hq = models.CharField(
        _("Head Quarter"),
        max_length=100,
        blank=True,
        null=True
    )
    company_size = models.CharField(
        _("Company Size"),
        max_length=50,
        choices=Size_Choices.choices,
        blank=True,
        null=True
    )
    revenue = models.IntegerField(_("Revenue"), blank=True, null=True)
    year_of_form = models.CharField(_("Year Of Form"), max_length=4, blank=True, null=True)

