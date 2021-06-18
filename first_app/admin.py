from django.contrib import admin
from .models import Products
# Register your models here.



class TagAdminView(admin.ModelAdmin):
    list_display = ['name', 'price', 'countInStock']
    # list_filter = ['name']
    search_fields = ['name']


admin.site.register(Products, TagAdminView)
