from django.db import models
from django.utils.translation import gettext as _

from assessment.models import Question, Assessment


class TrueFalseQuestion(Question):

    assessment = models.ForeignKey(
        Assessment,
        on_delete = models.CASCADE,
        verbose_name = _("Assessment"),
        related_name = 'tf_questions'
    )
    is_true = models.BooleanField(
        default=False,
        help_text="Is This True?",
        verbose_name=_("Is True")
    )

    def check_if_true(self, guess):
        if guess == True:
            guess_bool = True
        elif guess == False:
            guess_bool = False
        else:
            return False

        if guess_bool == self.is_true:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.id}-{self.content}'
    

    class Meta:
        verbose_name = _("True False Question")
        verbose_name_plural = _("True False Questions")
        ordering = ['topic']


