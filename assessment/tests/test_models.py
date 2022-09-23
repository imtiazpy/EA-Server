from django.test import TestCase
from django.shortcuts import get_object_or_404

from ..models import Assessment
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
        Assessment.objects.create(
            creator = user,
            title="Python Programmer test"
        )

    def test_assessment_str(self):
        assessment = get_object_or_404(Assessment, title='Python Programmer test')
        self.assertEqual(assessment.__str__(), f'Assessment-{assessment.id}-{assessment.title}')

    def test_assessment_title_max_length(self):
        assessment = get_object_or_404(Assessment, title='Python Programmer test')
        max_length = assessment._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_assessment_valid_user(self):
        user = get_object_or_404(CustomUser, name='employer')
        assessment = get_object_or_404(Assessment, id=1)
        self.assertEqual(assessment.creator, user)
