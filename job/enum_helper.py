from django.db import models

class JobType(models.IntegerChoices):

    FULL_TIME = 1, 'Full Time'
    PART_TIME = 2, 'Part Time'
    INTERNSHIP = 3, 'Internship'


class JobCategory(models.TextChoices):

    WEB_DESIGN = 'WEB_DESIGN', 'Web Design'
    WEB_DEVELOPMENT = 'WEB_DEVELOPMENT', 'Web Development'
    FULLSTACK = 'FULL_STACK', 'Full Stack'
    MOBILE_DEVELOPMENT = 'MOBILE_DEVELOPMENT', 'Mobile Development'