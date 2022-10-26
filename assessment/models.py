from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

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
    title = models.CharField(
        _("Title"), 
        max_length=100, 
        blank=False, 
        null=False,
        help_text=_("Title of your Assessment")
    )
    duration = models.DurationField(_("Duration"), null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')

    def __str__(self):
        return f'Assessment-{self.id}-{self.title}'

class QuestionTopic(models.Model):
    """Model definition for Question topic"""

    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Model definition for Question that is used in Assessment"""

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




