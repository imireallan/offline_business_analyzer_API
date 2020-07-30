from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import retrieve_business_by_owner, BusinessListView, BusinessRUDView, RegisterBusiness


# SimpleTestCase is used anytime you don't
# have to interact with the database
class TestUrls(SimpleTestCase):

	def test_register_business_url_is_resolved(self):
		url = reverse('business:register-business')
		self.assertEqual(resolve(url).func.view_class, RegisterBusiness)

	def test_business_detail_url_is_resolved(self):
		url = reverse('business:business-detail', args=['facebook'])
		self.assertEqual(resolve(url).func.view_class, BusinessRUDView)

	def test_business_owner_url_is_resolved(self):
		url = reverse('business:business-owner')
		self.assertEqual(resolve(url).func, retrieve_business_by_owner)

	def test_business_list_url_is_resolved(self):
		url = reverse('business:business-list')
		self.assertEqual(resolve(url).func.view_class, BusinessListView)
