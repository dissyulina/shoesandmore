from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('view_bag'))
        self.assertTemplateUsed(response, 'bag/bag.html')


class TestAddToBagViews(TestCase):
    """ Class to test the add_to_bag views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.quantity = 1
        self.filled_bag = {}

    def test_url_exists(self):
        """ Test view add to bag """
        url = f'/bag/add/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "add_to_bag")

    def test_can_add_to_bag(self):
        """ Test if a product can be added to bag successfully """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        post_data = {
            'bag_item': self.product,
            'quantity': int(self.quantity),
            'redirect_url': '/products/1/'
        }
        response = self.client.post('/bag/add/1/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['1'], 1)


class TestAdjustBagViews(TestCase):
    """ Class to test the adjust_bag views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.quantity = 1
        self.filled_bag = {'1': 1, '3': 1}

    def test_url_exists(self):
        """ Test view adjust bag """
        url = f'/bag/adjust/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "adjust_bag")

    def test_can_adjust_bag(self):
        """ Test if the bag can be adjusted successfully """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        post_data = {
            'bag_item': self.product,
            'quantity': int(self.quantity + 1)
        }
        response = self.client.post('/bag/adjust/1/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['1'], 2)


class TestRemoveFromBagViews(TestCase):
    """ Class to test the remove_from_bag views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.filled_bag = {'1': 1, '2': 1}

    def test_url_exists(self):
        """ Test view adjust bag """
        url = f'/bag/remove/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "remove_from_bag")

    def test_can_remove_from_bag(self):
        """ Test if the item can be successfully removed from bag"""
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        response = self.client.post('/bag/remove/1/')
        self.assertEqual(response.status_code, 200)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)
