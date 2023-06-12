from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnacksTest(SimpleTestCase):
    def test_homePage(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_homePageStatus(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aboutPage(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        
    def test_aboutPageStatus(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
