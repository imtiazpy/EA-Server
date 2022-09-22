from urllib import response
from django.test import TestCase
from django.shortcuts import get_object_or_404

from employers.models.profile import EmployerProfile

from .models import CustomUser

# Create your tests here.

class EmployerUserTypeTestCase(TestCase):

    def setUp(self):
        CustomUser.objects.create(
            email="employer@test.com", 
            name="employer", 
            type="EMPLOYER",
            password="testpass",
        )

    def test_employer_type(self):
        user = get_object_or_404(CustomUser, name="employer")
        self.assertEqual(user.type, 'EMPLOYER')


class JobSeekerUserTypeTestCase(TestCase):
    
    def setUp(self):
        CustomUser.objects.create(
            email="jobseeker@test.com",
            name="job seeker",
            type="JOB_SEEKER",
            password="testpass"
        )
    
    def test_job_seeker_type(self):
        user = get_object_or_404(CustomUser, name="job seeker")
        self.assertEqual(user.type, 'JOB_SEEKER')


class AuthUserSignUpAPITest(TestCase):
    data = {
        "email": "user@test.com",
        "name": "user",
        "type": "JOB_SEEKER",
        "password": "testpassword",
        "re_password": "testpassword"
    }
    
    def test_signup_url_response(self):
        url = '/api/v1/auth/users/'
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)


    
