from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Assessment(models.Model):
    """Model definition for the Assessment"""

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)
    questions = models.ManyToManyField('assessment.Question')
    duration = models.DurationField(_("Duration"), null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Assessment-{self.id}-{self.title}'



class QuestionTopic(models.Model):
    """Model definition for Question topic"""

    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Model definition for Question that is used in Assessment"""

    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)
    topic = models.ForeignKey('assessment.QuestionTopic', on_delete=models.CASCADE, related_name='question')
    choices = models.ManyToManyField('assessment.Choice')
    duration = models.DurationField(_("Duration"), null=True, blank=True)

    def __str__(self):
        return f'{self.topic.__str__()}-{self.title}'


class QuestionSet(models.Model):
    """Model definition for question set"""
    assessment = models.ForeignKey('assessment.Assessment', on_delete=models.CASCADE, related_name='question_set')
    question = models.ForeignKey('assessment.Question', on_delete=models.CASCADE, related_name='question_set')

    def __str__(self):
        return f'Question set of {self.assessment.__str__()}'


class Choice(models.Model):
    """Model definition for Choice"""

    title = models.CharField(_("Title"), max_length=100, blank=False, null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ChoiceSet(models.Model):
    """Model definition for ChoiceSet"""

    question = models.ForeignKey('assessment.Question', on_delete=models.CASCADE, related_name='choice_set')
    choice = models.ForeignKey('assessment.Choice', on_delete=models.CASCADE, related_name='choice_set')

    def __str__(self):
        return f'{self.question.title}-{self.choice.title}'


