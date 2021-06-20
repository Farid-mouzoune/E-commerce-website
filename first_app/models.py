from django.core.checks.messages import CRITICAL
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField


# Create your models here.



class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(default=0, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    ceatedAt = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True)
    comment = models.TextField(max_length=250, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=20, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    PaidAt = models.DateTimeField(auto_now_add=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(null=True)
    
    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    qty = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    postalCode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    ShippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return str(self.Address)
