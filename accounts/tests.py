from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="3u9oK@example.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="4nSjL@example.com",
            password="testpass123",
        )
        self.assertTrue(admin_user.is_superuser)
