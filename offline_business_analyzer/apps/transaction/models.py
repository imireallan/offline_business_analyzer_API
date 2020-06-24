from django.db import models
from offline_business_analyzer.apps.business.models import Business
from django.conf import settings


class Order(models.Model):
	STATUS = [
		('PENDING', 'pending'),
		('ACCEPTED', 'accepted'),
		('REJECTED', 'rejected'),
		('COMPLETED', 'completed'),
	]
	item = models.CharField(max_length=100)
	customer = models.CharField(max_length=100)
	quantity = models.IntegerField()
	unit_amount = models.DecimalField(decimal_places=4, max_digits=19)
	total_transaction = models.DecimalField(decimal_places=4, max_digits=19)
	order_id = models.IntegerField()
	status = models.CharField(max_length=20, choices=STATUS, default='pending')
	transaction_date = models.DateField()
	due_date = models.DateField()

	def __str__(self):
		return str(self.order_id)


class OrderPayment(models.Model):
	order_number = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_payments')
	customer = models.CharField(max_length=100)
	transaction_date = models.DateField()

	def __str__(self):
		return str(self.order_number)


class Bill(models.Model):
	STATUS = [
		('OPEN', 'open'),
		('CLOSED', 'closed'),
	]
	bill_number = models.IntegerField()
	status = models.CharField(max_length=10, choices=STATUS, default='open')
	supplier = models.CharField(max_length=100)
	unit_amount = models.DecimalField(decimal_places=4, max_digits=19)
	total_transaction = models.DecimalField(decimal_places=4, max_digits=19)
	transaction_date = models.DateField()
	item = models.CharField(max_length=100)
	due_date = models.DateField()
	quantity = models.IntegerField()

	def __str__(self):
		return str(self.bill_number)


class BillPayment(models.Model):
	bill_number = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bills_payment')
	supplier = models.CharField(max_length=100)
	transaction_date = models.DateField()

	def __str__(self):
		return str(self.bill_number)


class Transaction(models.Model):
	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='transactions', default=1)
	orders = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
	bills = models.ForeignKey(Bill, on_delete=models.CASCADE, default=1)
	csv_file = models.FileField(upload_to='csv_file', blank=True, null=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.csv_file)
