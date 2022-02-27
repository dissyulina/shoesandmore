from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from products.models import Product

from .models import Favorites, FavoritesItem


class TestFavoritesViews(TestCase):
    """ Class to test the view_favorites views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email="user@mail.com",
                        password='pswd123')

    def test_url_response(self):
        """ Test URL response success """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        response = self.client.get('/favorites/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        response = self.client.get(reverse('view_favorites'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        response = self.client.get(reverse('view_favorites'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'favorites/favorites.html')


class TestAddToFavoritesViews(TestCase):
    """ Class to test the add_to_favorites views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email="user@mail.com",
                        password='pswd123')
        self.product = Product.objects.create(name="testproduct",
                                              price=50.00)

    def test_url_exists(self):
        """ Test view add to favorites """
        url = f'/favorites/add_to_favorites/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "add_to_favorites")
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        self.assertTrue(login)

    def test_can_add_to_favorites(self):
        """ Test if a product can be added successfully """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        response = self.client.get(
            f'/favorites/add_to_favorites/{self.product.id}/'
            )
        existing_items = FavoritesItem.objects.filter(product=self.product.id)
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(existing_items), 1)


class TestRemoveFromFavoritesViews(TestCase):
    """ Class to test the remove_from_favorites views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email="user@mail.com",
                        password='pswd123')
        self.product = Product.objects.create(
                       name="testproduct",
                       price=50.00)
        self.favorites = Favorites.objects.create(
                         user=self.test_user)
        self.favorite_item = FavoritesItem.objects.create(
                             favorites=self.favorites,
                             product=self.product)

    def test_url_exists(self):
        """ Test view add to favorites """
        url = f'/favorites/remove_from_favorites/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "remove_from_favorites")
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        self.assertTrue(login)
