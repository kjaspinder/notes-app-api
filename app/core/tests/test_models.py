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

    def test_new_user_email_normalized(self):
        """test that the email of new user is normalized"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            first_name='first_name',
            last_name='last_name',
            gender=1,
            password='test_123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_details(self):
        """test creating user with incomplete details raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='test@gmail.com',
                first_name='first_name',
                last_name=None,
                gender=1,
                password='test_123'
                )

    def test_create_new_superuser(self):
        """test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            first_name='first_name',
            last_name='last_name',
            gender=1,
            password='test_123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
