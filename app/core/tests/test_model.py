from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'mike@GmAiL.CoM'
        user = get_user_model().objects.create_user(
            email, 'test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_for_a_not_correct_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Bla')

    def test_create_super_user(self):
        """Testing to see if superuser is created"""
        user = get_user_model().objects.create_superuser(
            'test@bla.nl',
            'test234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
