from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from spharm.views import map, analogies, pharmacy, recommendations


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('map')
        print(resolve(url))
