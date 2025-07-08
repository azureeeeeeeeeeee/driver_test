from django.contrib import admin
from data.models import Driver, Rute, Transaksi

# Register your models here.
admin.site.register(Transaksi)
admin.site.register(Driver)
admin.site.register(Rute)