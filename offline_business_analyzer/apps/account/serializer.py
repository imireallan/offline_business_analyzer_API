from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
	password_2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ('email', 'username', 'password', 'password_2')
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def save(self):
		user = User(
			email=self.validated_data['email'],
			username=self.validated_data['username']
		)
		password = self.validated_data['password']
		password2 = self.validated_data['password_2']

		if password != password2:
			raise serializers.ValidationError({'password': 'passwords must match.'})

		user.set_password(password)
		user.save()
		return user
