from django.contrib import admin
from .models import Products, Order, OrderItem, Review
# Register your models here.



class TagProductAdminView(admin.ModelAdmin):
    list_display = ['name', 'price', 'countInStock']
    # list_filter = ['name']
    search_fields = ['name']



admin.site.register(Products, TagProductAdminView)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
