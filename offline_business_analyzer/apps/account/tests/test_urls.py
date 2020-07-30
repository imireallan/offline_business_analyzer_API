from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rest_framework.authtoken.views import obtain_auth_token

from ..views import registration_view


# SimpleTestCase is used anytime you don't
# have to interact with the database
class TestUrls(SimpleTestCase):

	def test_register_user_url_is_resolved(self):
		url = reverse('account:register-user')
		self.assertEqual(resolve(url).func, registration_view)

	def test_login_url_is_resolved(self):
		url = reverse('account:login')
		self.assertEqual(resolve(url).func, obtain_auth_token)
