from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
class TestCustomUser:
    user = get_user_model()

    def test_create_user(self):
        user = self.user.objects.create_user(
            username="testuser",
            email="3u9oK@example.com",
            password="testpass123",
        )
        assert user.username == "testuser"

    def test_create_superuser(self):
        admin_user = self.user.objects.create_superuser(
            username="superadmin",
            email="4nSjL@example.com",
            password="testpass123",
        )
        assert admin_user.is_superuser is True
