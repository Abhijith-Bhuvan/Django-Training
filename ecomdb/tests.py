from ecomdb.views import home
from django.urls import reverse,resolve
from django.test import TestCase

# Create your tests here.

class Hometests(TestCase):
    def test_home_view_statuscode(self):
        url = reverse('Home_page')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)