from rest_framework import serializers
from .models import Transaction, OrderPayment, Order, BillPayment, Bill
from offline_business_analyzer.apps.business.models import Business

from .utils import validate_csv


class TransactionSerializer(serializers.ModelSerializer):
	business = serializers.StringRelatedField()
	orders = serializers.StringRelatedField()
	bills = serializers.StringRelatedField()
	created_by = serializers.StringRelatedField()

	class Meta:
		model = Transaction
		fields = '__all__'

	def save(self):
		csv_file = self.validated_data.get('csv_file', None)
		created_by = self.context.get('user', None)

		# get business by owner
		business = Business.objects.filter(owner=created_by).first()

		# create a transaction instance
		transaction = Transaction(
			created_by=created_by,
			csv_file=csv_file,
			business=business
		)
		validate_csv(csv_file, transaction)


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		models = Order
		fields = '__all__'


class OrderPaymentSerializer(serializers.ModelSerializer):
	order_number = serializers.StringRelatedField()

	class Meta:
		model = OrderPayment
		fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bill
		fields = '__all__'


class BillPaymentSerializer(serializers.ModelSerializer):
	bill_number = serializers.StringRelatedField()

	class Meta:
		model = BillPayment
		fields = '__all__'
