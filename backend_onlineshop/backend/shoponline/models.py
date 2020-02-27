from django.db import models
from django.utils import timezone
# Create your models here.
class Products(models.Model):
    productname=models.CharField(max_length=200)
    productdescription=models.CharField(max_length=200)
    productcategory=models.CharField(max_length=200)
    productprice=models.CharField(max_length=200)
    productImage= models.ImageField(max_length=None)
    productseller= models.CharField(max_length=200)
    isBestproduct= models.BooleanField()
    isTopproduct= models.BooleanField()
    productrating= models.IntegerField()

class ShippingDetail(models.Model):
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    shippingDate=models.CharField(max_length=200)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    userId=models.CharField(max_length=200)
    totalPrice=models.CharField(max_length=200)

class Users(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    fullname=models.CharField(max_length=200)
    email=models.EmailField()
    isAdmin=models.BooleanField(default=False)
    password=models.CharField(max_length=200,null=True)
    createdon=models.TimeField(default=timezone.now)



# var UserSchema = new Schema({
#     firstName: String,
#     lastName: String,
#     fullName: String,
#     email: String,
#     isAdmin: Boolean,
#     password: String,
#     createdOn: String
# })
