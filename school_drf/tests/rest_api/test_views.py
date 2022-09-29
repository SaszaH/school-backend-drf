import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import get_user_model


user = get_user_model()

class TestApiExam(APITestCase):
    @pytest.mark.django_db
    def test_exam_view(self):
        url = reverse("api:exams-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
