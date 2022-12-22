from django.db import models
from django.utils.translation import gettext as _

from assessment.models import Assessment, Question

class MCQuestion(Question):
    """Extending Question model for Multiple Choice"""

    assessment = models.ForeignKey(
        Assessment, 
        on_delete=models.CASCADE,
        related_name="mc_questions",
        verbose_name = _("Assessment")
    )

    def check_if_correct(self, guess):
        """
        If the choice is correct, return True, otherwise return False
        
        :param guess: the id of the choice that the user selected
        """
        choice = Choice.objects.get(id=guess)
        if choice.is_correct is True:
            return True
        return False

    def get_choices(self):
        """
        It returns a QuerySet of all the choices associated with this question
        :return: A list of Choice objects associated with the Question.
        """
        return Choice.objects.filter(question=self)

    def get_choices_list(self):
        """
        It returns a list of tuples, where each tuple contains the id and content of a choice
        :return: A list of tuples.
        """
        return [(choice.id, choice.content) for choice in Choice.objects.filter(question=self)]
    
    class Meta:
        verbose_name = _("Multiple Choice Question")
        verbose_name_plural = _("Multiple Choice Questions")
        ordering = ['topic']
    
    def __str__(self):
        return f'{self.id}-{self.content}'


class Choice(models.Model):
    """Model definition for Multiple Choice Answers"""

    question = models.ForeignKey(
        MCQuestion, 
        on_delete=models.CASCADE, 
        verbose_name=_("Question"),
        related_name='choices'
    )

    content = models.CharField(
        max_length=1000,
        blank=False,
        help_text=_("Enter the text that you want displayed as choice"),
        verbose_name=_("Content")
    )

    is_correct = models.BooleanField(
        default=False, 
        help_text=_("Is this correct answer?"), 
        verbose_name=_("Is Correct")
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

