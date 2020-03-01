from django.contrib import admin
from inventory.models import Item, Manufacturer, Transaction

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Item)
admin.site.register(Transaction)