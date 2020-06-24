from django.contrib import admin
from .models import Transaction, Order, OrderPayment, Bill, BillPayment


class CustomOrderAdmin(admin.ModelAdmin):
	list_display = ('item', 'customer', 'quantity', 'unit_amount', 'order_id', 'status', 'transaction_date', 'due_date',
					'total_transaction')
	search_fields = ('item', 'customer')
	readonly_fields = ('transaction_date', 'due_date',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class CustomOrderPaymentAdmin(admin.ModelAdmin):
	list_display = ('order_number', 'customer', 'transaction_date')
	search_fields = ('order_number', 'customer_name', 'owner')
	readonly_fields = ('transaction_date',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class CustomBillAdmin(admin.ModelAdmin):
	list_display = (
		'supplier', 'bill_number', 'unit_amount', 'status', 'transaction_date', 'due_date', 'total_transaction')
	search_fields = ('bill_number', 'supplier')
	readonly_fields = ('transaction_date', 'due_date',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class CustomBillPaymentAdmin(admin.ModelAdmin):
	list_display = ('bill_number', 'supplier', 'transaction_date')
	search_fields = ('bill_number', 'supplier')
	readonly_fields = ('transaction_date',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class CustomTransactionAdmin(admin.ModelAdmin):
	list_display = ('csv_file', 'created_by', 'created_at')
	search_fields = ('csv_file',)
	readonly_fields = ('created_by', 'created_at')

	def save_model(self, request, obj, form, change):
		obj.created_by = request.user

		super(CustomTransactionAdmin, self).save_model(request, obj, form, change)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Transaction, CustomTransactionAdmin)
admin.site.register(Order, CustomOrderAdmin)
admin.site.register(OrderPayment, CustomOrderPaymentAdmin)
admin.site.register(Bill, CustomBillAdmin)
admin.site.register(BillPayment, CustomBillPaymentAdmin)
