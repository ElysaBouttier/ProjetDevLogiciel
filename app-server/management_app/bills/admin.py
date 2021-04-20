from django.contrib import admin
from .models import Bills
from .models import BillsProduct


# Register your models here.
admin.site.register(Bills)
admin.site.register(BillsProduct)