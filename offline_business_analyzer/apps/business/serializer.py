from rest_framework import serializers
from .models import Business


class BusinessSerializer(serializers.ModelSerializer):
	owner = serializers.StringRelatedField()

	class Meta:
		model = Business
		fields = '__all__'
		read_only_fields = ('id', 'owner')

