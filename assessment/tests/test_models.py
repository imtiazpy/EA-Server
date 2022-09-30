from django.test import TestCase
from django.shortcuts import get_object_or_404

from ..models import (
    Assessment, 
    MCQuestion, 
    Choice,
    QuestionTopic, 
    TrueFalseQuestion, 
    ShortAnswerQuestion, 
    Answer
)
from users.models import CustomUser

class ModelTestCase(TestCase):
    """Test case to test Models"""

    def setUp(self):
        user = CustomUser.objects.create(
            email="employer@test.com", 
            name="employer", 
            type="EMPLOYER",
            password="testpass",
        )
        assessment = Assessment.objects.create(
            created_by = user,
            title="Python Programmer test"
        )

        topic = QuestionTopic.objects.create(title='Programming Language')

        mcq = MCQuestion.objects.create(
            content="What is Python?",
            topic=topic,
            assessment=assessment
        )

        choice = Choice.objects.create(
            question = mcq,
            content = 'A programming language.',
            is_correct = True
        )

    def test_assessment_str(self):
        assessment = get_object_or_404(Assessment, title='Python Programmer test')
        self.assertEqual(assessment.__str__(), f'Assessment-{assessment.id}-{assessment.title}')

    def test_assessment_title_max_length(self):
        assessment = get_object_or_404(Assessment, title='Python Programmer test')
        max_length = assessment._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_assessment_user(self):
        user = get_object_or_404(CustomUser, name='employer')
        assessment = get_object_or_404(Assessment, id=1)
        self.assertEqual(assessment.created_by, user)

    # def test_mcQuestion_with_choices(self):
    #     q = get_object_or_404(MCQuestion, assessment=1)
    #     c = Choice.objects.filter(question=q)

    #     self.assertEqual(q.get_choices(), c)

    def test_choice_correct(self):
        q = get_object_or_404(MCQuestion, assessment=1)
        c = Choice.objects.first()
        self.assertEqual(q.check_if_correct(1), c.is_correct)

