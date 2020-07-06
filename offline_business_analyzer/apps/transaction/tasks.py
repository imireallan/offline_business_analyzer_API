from __future__ import absolute_import, unicode_literals
import logging
from dateutil.parser import parse

from celery import shared_task
from .models import Order, Bill, Transaction
from offline_business_analyzer.apps.business.models import Business


logger = logging.getLogger(__name__)


def format_dates(date_string):
	return parse(date_string).date()


@shared_task
def save_csv_data_to_db(transaction, bills, orders):
	logger.warning('Saving transaction......')
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
			transaction_id=transaction.id
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
		logger.warning('Finished processing csv')

	except Exception as e:
		logger.error(e)
		raise e

