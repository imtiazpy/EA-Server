from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

class AssessmentTypes(models.TextChoices):
    """Types choices for Assessment"""

    MCQ = "MCQ", "MCQ"
    SHORT_ANSWER = "SHORT_ANSWER", "Short Answer"
    TRUE_FALSE = "TRUE_FALSE", "True False"
    
class Assessment(models.Model):
    """Model definition for the Assessment"""

    type = models.CharField(
        _("Type"), 
        max_length=50, 
        choices=AssessmentTypes.choices, 
        blank=False
    )
    slug = models.SlugField(_('Slug'), max_length=6, blank=True, null=True)
    title = models.CharField(
        _("Title"), 
        max_length=100, 
        blank=False, 
        null=False,
        help_text=_("Title of your Assessment")
    )
    duration = models.DurationField(_("Duration"), null=True, blank=True)
    is_public = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(6)
            duplicate_slug = True
            while duplicate_slug:
                other_obj_with_same_slug = type(self).objects.filter(slug=self.slug)
                if len(other_obj_with_same_slug) > 0:
                    self.slug = get_random_string(6)
                else:
                    duplicate_slug = False
            super(Assessment, self).save(*args, **kwargs)

            

    def __str__(self):
        return f'Assessment-{self.id}-{self.title}'

class QuestionTopic(models.Model):
    """Model definition for Question topic"""

    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


# The Question class is an abstract class that defines the content and topic of a question
class Question(models.Model):
    """Model definition for Question"""

    content = models.CharField(
        _("Content"), 
        max_length=1000, 
        blank=False, 
        null=False, 
        help_text=_("Enter you question")
    )
    topic = models.ForeignKey(
        'assessment.QuestionTopic', 
        on_delete=models.CASCADE, 
        verbose_name = _("Topic")
    )

    class Meta:
        abstract = True


# The Result class is a model that stores the marks obtained by a job seeker in an assessment
class Result(models.Model):
    """Model definition of Result"""

    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Marks")
    )
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Result-{self.assessment.title}'






