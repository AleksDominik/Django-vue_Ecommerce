from django.contrib import admin

# Register your models here.
from .models import Products,ShippingDetail,Users

admin.site.register(Products)
admin.site.register(ShippingDetail)
admin.site.register(Users)
