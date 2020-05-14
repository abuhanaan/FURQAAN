from django.contrib import admin
from inventory.models import Item, Manufacturer, Transaction, Log

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'maker', 'quantity', 'priceByDefault']
    search_fields = ['item_name']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['trans_id', 'quantity', 'item', 'sellPrice', 'user',
                    'imei', 'custName', 'custAdd', 'cusPhone']
    search_fields = ['trans_id', 'imei', 'cusPhone']


admin.site.register(Manufacturer)
admin.site.register(Item, ItemAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Log)
