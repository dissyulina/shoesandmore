from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog


class TestAllArticlesViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('all_articles'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('all_articles'))
        self.assertTemplateUsed(response, 'blogs/articles.html')


class TestIndividualArticleViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        user = User.objects.create(username='user', email="user@mail.com", password="pswd123")
        blog = Blog.objects.create(author=user, title='Test', paragraph1='Blog example')
        response = self.client.get(f'/blogs/{blog.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        user = User.objects.create(username='user', email="user@mail.com", password="pswd123")
        blog = Blog.objects.create(author=user, title='Test', paragraph1='Blog example')
        response = self.client.get(f'/blogs/{blog.id}')
        self.assertTemplateUsed(response, 'blogs/article.html')
