from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.



class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(default=0, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    ceatedAt = DateTimeField(auto_now_add=True)
    # _id = models.AutoField(primary_key=True, editable=False)




    def __str__(self):
        return self.name

