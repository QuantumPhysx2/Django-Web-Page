from django.contrib import admin
from application_file.models import Customer, Vehicle, Manufacturer

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Manufacturer)
