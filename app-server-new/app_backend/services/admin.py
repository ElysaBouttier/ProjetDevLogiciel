from django.contrib import admin
from .models import Bill, BillProduct, Client, Product

# Register your models here.
# admin.site.register(BillProduct)
# admin.site.register(Client)
# admin.site.register(Product)

class BillAdmin(admin.ModelAdmin):
    list_display = ('idClient', 'price', 'isPaid')
class BillProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'idBills', 'idProduct')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstName', 'mail', 'registrationDate')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')

admin.site.register(Bill, BillAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(BillProduct, BillProductAdmin)
admin.site.register(Product, ProductAdmin)