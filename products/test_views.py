from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class TestProductsViews(TestCase):
    """ Class to test the all_products views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products/products.html')


class TestIndividualProductViews(TestCase):
    """ Class to test the all_products views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get(f'/products/{self.product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(f'/products/{self.product.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')
