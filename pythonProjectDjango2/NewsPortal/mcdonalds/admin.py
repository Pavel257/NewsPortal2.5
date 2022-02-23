from django.contrib import admin

from mcdonalds.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('time_in', 'time_out', 'cost', 'take_away', 'complete')
    list_filter = ('time_in', 'time_out', 'cost', 'take_away', 'complete')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    list_display_links = ('name',)