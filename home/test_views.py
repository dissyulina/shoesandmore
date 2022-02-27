from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_index(self):
        """
        Check the response status and
        check if it's using the right template
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
