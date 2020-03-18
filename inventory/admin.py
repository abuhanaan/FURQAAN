from django.contrib import admin
from inventory.models import Item, Manufacturer, Transaction

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'maker', 'quantity', 'priceByDefault']
    search_fields = ['item_name']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['trans_id', 'quantity', 'item', 'sellPrice', 'imei', 'custName', 'custAdd', 'cusPhone']
    search_fields = ['trans_id', 'imei', 'cusPhone']


admin.site.register(Manufacturer)
admin.site.register(Item, ItemAdmin)
admin.site.register(Transaction, TransactionAdmin)
