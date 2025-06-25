from django.test import TestCase
from django.urls import reverse
from .models import ShortURL

class ShortenerTest(TestCase):
    def test_create_and_redirect(self):
        url = "https://example.com/test"
        obj = ShortURL.objects.create(original_url=url)
        response = self.client.get(f'/{obj.short_code}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, url)
