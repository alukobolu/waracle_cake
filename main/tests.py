from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class CakeTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("cakes")

    def test_get_cakes(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_post_cakes(self):

        sample_data = {
            "name": "test cake",
            "comment": "test comment",
            "imageURL": "/test_url",
            "yumFactor": 1
        }
        response = self.client.post(self.url, sample_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["success"], "Successfully created")
