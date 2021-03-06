from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEquals = (found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('index.html')
        self.assertEquals(response.content.decode(), expected_html)

    def test_home_page_redirects_on_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['users_code'] ='def my_function(): pass'
        response = index(request)

        self.assertEqual(response.status_code, 302)
        self.assetEqual(response['location'], '/')
