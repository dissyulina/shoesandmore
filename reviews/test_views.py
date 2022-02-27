from django.test import TestCase, Client
from django.urls import resolve
from django.contrib.auth.models import User
from products.models import Product


class TestAddReviewView(TestCase):
    """ Class to test the add_review views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser', email="user@mail.com", password='pswd123')
        self.product = Product.objects.create(name="testproduct",
                                              price=50.00)

    def test_url_exists(self):
        """ Test view add to favorites """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        url = f'/reviews/add_review/{self.product.id}/'
        found = resolve(url)
        self.assertTrue(login)
        self.assertEqual(found.url_name, "add_review")

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        login = self.client.login(username=self.test_user.username,
                                  password='pswd123')
        response = self.client.get(f'/reviews/add_review/{self.product.id}/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')
