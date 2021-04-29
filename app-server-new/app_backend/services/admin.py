from django.contrib import admin
from .models import Bill, BillProduct, Client, Product

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillProduct)
admin.site.register(Client)
admin.site.register(Product)