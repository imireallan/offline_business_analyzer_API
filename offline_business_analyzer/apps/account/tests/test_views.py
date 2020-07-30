import json
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_user = reverse('account:register-user')
		self.login = reverse('account:login')
		self.register_user_data = {
			"email": "test@gmail.com",
			"username": "test",
			"password": "password",
			"password2": "password"
		}
		self.register_user_password_mismatch = {
			"email": "test@gmail.com",
			"username": "test",
			"password": "password",
			"password2": "passward"
		}

		self.login_data = {
			"username": "test@gmail.com",
			"password": "password"
		}

	def test_user_registration_success(self):
		response = self.client.post(self.register_user, self.register_user_data)
		self.assertEqual(response.status_code, 201)

	def test_user_registration_with_password_mismatch(self):
		response = self.client.post(self.register_user, self.register_user_password_mismatch)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.json()["password"], "passwords must match.")

	def test_user_cannot_login_without_signup(self):
		response = self.client.post(self.login, self.login_data)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.json()["non_field_errors"], ['Unable to log in with provided credentials.'])

	def test_user_can_login_after_signup(self):
		register_response = self.client.post(self.register_user, self.register_user_data)
		response = self.client.post(self.login, self.login_data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()["token"],register_response.json()["token"])




