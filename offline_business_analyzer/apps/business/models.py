from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Business(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='businesses')
	name = models.CharField(max_length=100, unique=True)
	business_abbr = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)
	annual_sales_revenue = models.DecimalField(decimal_places=4, max_digits=19)
	accounting_software = models.CharField(max_length=30, null=True, blank=True)
	country = models.CharField(max_length=100, default="United States of America", blank=True, null=True)
	countries_of_operation = ArrayField(models.CharField(max_length=100, blank=True, null=True))
	entity = models.CharField(max_length=20, blank=True, null=True)
	date_registered = models.DateTimeField(verbose_name='date registered', auto_now_add=True)

	def __str__(self):
		return self.name
