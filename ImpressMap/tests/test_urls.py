from django.test import SimpleTestCase
from django.urls import reverse, resolve

from impresses.views import CreateImpress

from impresses.views import home_page


class TestUrls(SimpleTestCase):

    def test_add_url_resolvers(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class, CreateImpress)

    def test_home_page_url_resolvers(self):
        url = reverse('homePage')
        self.assertEqual(resolve(url).func, home_page)
#
