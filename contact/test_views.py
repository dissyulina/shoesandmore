from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact

class TestContactViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_can_send_contact_form(self):
        """ 
        Check if the form is sent successfully
        and if it redirects back to contact page
        """
        response = self.client.post('/contact/', {'name': 'User',
                                                  'email': 'test@mail.com',
                                                  'message': 'test'})
        self.assertRedirects(response, '/contact/')


class TestFAQViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/contact/faq/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('faq'))
        self.assertTemplateUsed(response, 'contact/faq.html')
