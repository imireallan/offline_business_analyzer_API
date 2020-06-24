import csv
import io
from dateutil.parser import parse
from collections import Counter
from rest_framework import serializers
from .models import Order, Bill

HEADERS_ALLOWED = [
	'Transaction',
	'ID',
	'Status',
	'Transaction Date',
	'Due Date',
	'Customer or Supplier',
	'Item',
	'Quantity',
	'Unit Amount',
	'Total Transaction Amount'
]


def format_dates(date_string):
	return parse(date_string).date()


def filter_transactions(items, orders, bills):
	if 'Order' in items:
		orders.append(items)
	elif 'Bill' in items:
		bills.append(items)


def validate_csv_headers(csv_file, transaction):
	if not csv_file.name.endswith('.csv'):
		raise serializers.ValidationError('please upload a csv file')
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	headers = next(io_string).strip().split(',')
	if Counter(headers) != Counter(HEADERS_ALLOWED):
		raise serializers.ValidationError('Csv file should contain all the headers')
	orders = []
	bills = []
	for column in csv.reader(io_string, delimiter=','):
		filter_transactions(column, orders, bills)

	# save transaction in the db
	transaction.save()
	bills_model_instance = []
	orders_model_instance = []
	for bill in bills:
		bills_model_instance.append(Bill(
			bill_number=bill[1],
			status=bill[2].upper(),
			unit_amount=bill[8],
			total_transaction=bill[9],
			transaction_date=format_dates(bill[3]),
			due_date=format_dates(bill[4]),
			supplier=bill[5],
			item=bill[6],
			quantity=bill[7],
			transaction=transaction
		))

	for order in orders:
		orders_model_instance.append(Order(
			order_id=order[1],
			status=order[2].upper(),
			unit_amount=order[8],
			total_transaction=order[9],
			transaction_date=format_dates(order[3]),
			due_date=format_dates(order[4]),
			customer=order[5],
			quantity=order[7],
			item=order[6],
			transaction=transaction
		))

	try:
		Bill.objects.bulk_create(bills_model_instance)
		Order.objects.bulk_create(orders_model_instance)
		return transaction

	except Exception as e:
		raise e
