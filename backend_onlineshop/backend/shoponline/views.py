from django.shortcuts import render

from django.http import HttpResponse
from models import Products,Users,ShippingDetail


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#product api 

def CreateProduct(request):
    data=request.POST
    prod=Product(
    productname=models.CharField(max_lenght)
    productdescription=models.CharField(max_length=200)
    productcategory=models.CharField(max_length=200)
    productprice=models.CharField(max_length=200)
    productImage= models.ImageField(max_length=None)
    productseller= models.CharField(max_length=200)
    isBestproduct= models.BooleanField()
    isTopproduct= models.BooleanField()
    productrating= models.IntegerField()
    )
