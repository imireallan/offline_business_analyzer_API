import io
import csv
import logging
from collections import Counter
from rest_framework import serializers

from .tasks import save_csv_data_to_db

logger = logging.getLogger(__name__)


def filter_transactions(items, orders, bills):
	if 'Order' in items:
		orders.append(items)
	elif 'Bill' in items:
		bills.append(items)


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


def validate_csv(csv_file, transaction):
	logger.warning('Starting CSV validation....')
	if not csv_file.name.endswith('.csv'):
		raise serializers.ValidationError({'error': 'please upload a csv file'})
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	headers = next(io_string).strip().split(',')
	if Counter(headers) != Counter(HEADERS_ALLOWED):
		raise serializers.ValidationError('Csv file should contain all the headers')
	logger.warning('Successfully validated CSV....')
	orders = []
	bills = []
	for column in csv.reader(io_string, delimiter=','):
		filter_transactions(column, orders, bills)
	save_csv_data_to_db.delay(transaction, bills, orders)

