from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import UserProfile


class TestProfilesViews(TestCase):
    """ Class to test the profiles views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email="user@mail.com",
                        password='pswd123')

    def test_url_response(self):
        """ Test URL response success """
        login = self.client.login(username='testuser',
                                  password='pswd123')
        response = self.client.get('/profile/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        login = self.client.login(username='testuser',
                                  password='pswd123')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        login = self.client.login(username='testuser',
                                  password='pswd123')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/profile.html')

