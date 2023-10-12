from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper_app.models import Topic, Newspaper


class ModelTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="test",
            password="123",
            first_name="Test",
            last_name="Test",
        )
        self.topic = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test Content",
            published_year="2023-01-01",
            topic=self.topic,
        )
        self.newspaper.redactors.add(self.redactor)

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} ({self.redactor.first_name} {self.redactor.last_name})",
        )

    def test_topic_str(self):
        self.assertEqual(str(self.topic), self.topic.name)

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), self.newspaper.title)

    def test_redactor_absolute_url(self):
        url = reverse("newspaper_app:redactor-detail", kwargs={"pk": self.redactor.pk})
        self.assertEqual(self.redactor.get_absolute_url(), url)

    def test_newspaper_redactors(self):
        self.assertEqual(self.newspaper.redactors.first(), self.redactor)
