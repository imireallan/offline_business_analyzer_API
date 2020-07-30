from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import upload_csv


# SimpleTestCase is used anytime you don't
# have to interact with the database
class TestUrls(SimpleTestCase):

	def test_register_business_url_is_resolved(self):
		url = reverse('transaction:upload_csv')
		self.assertEqual(resolve(url).func, upload_csv)
