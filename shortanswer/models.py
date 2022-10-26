from django.db import models
from django.utils.translation import gettext as _

from assessment.models import Assessment, Question


class ShortAnswerQuestion(Question):
    """Model definition for ShortAnswerQuestion model"""

    assessment = models.ForeignKey(
        Assessment,
        on_delete = models.CASCADE,
        related_name = "short_answer_questions",
        verbose_name = _("Assessment")
    )

    def get_answer(self, answer):
        return str(answer)

    
    def __str__(self):
        return f'{self.id}-{self.content}'
    
    class Meta:
        verbose_name = "Short Answer Question"
        verbose_name_plural = "Short Answer Questions"


class Answer(models.Model):
    """model definition for Answers"""

    question = models.OneToOneField(
        ShortAnswerQuestion,
        on_delete = models.CASCADE,
        verbose_name = _("Question")
    )

    content = models.TextField(
        _("Content"),
        max_length = 1000,
        blank = False,
        null = False,
        help_text = _("Write down the answer for the Short Answer Question")
    )

    def __str__(self):
        return f'{self.id}-{self.content}'

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
