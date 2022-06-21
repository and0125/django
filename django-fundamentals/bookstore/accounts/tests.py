from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUsertests(TestCase):

    ## Model Tests
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Aaron',
            email='and@aol.com',
            password='testing123'
        )
        self.assertEqual(user.username, 'Aaron')
        self.assertEqual(user.email, 'and@aol.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='Admin',
            email='admin@aol.com',
            password='testing123'
        )
        self.assertEqual(user.username, 'Admin')
        self.assertEqual(user.email, 'admin@aol.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)