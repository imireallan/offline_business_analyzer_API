from django.contrib import admin
from offline_business_analyzer.apps.business.models import Business


class CustomBusinessAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'business_abbr', 'country', 'entity', 'annual_sales_revenue', 'date_registered')
	search_fields = ('name', 'entity', 'owner')
	readonly_fields = ('date_registered',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Business, CustomBusinessAdmin)
