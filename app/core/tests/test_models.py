from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'testpass123'
        first_name = 'test'
        last_name = 'user'
        gender = 1
        user = get_user_model().objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.gender, gender)
        self.assertTrue(user.check_password(password))
