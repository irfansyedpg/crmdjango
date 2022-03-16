
from re import T
from statistics import mode
from tkinter import CASCADE
from unicodedata import decimal, name
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url       

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd=models.DateTimeField(auto_now=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transection_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)


    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for o in orderitems:
            if o.product.digital == False:
                shipping = True

        return shipping        


    @property 
    def get_cart_total(self):

        orderitems=self.orderitem_set.all() # so we went to child table get all order for this FK
        total=sum(item.get_total for item in orderitems) # it will call the get_total property in the child model(orderitem table) and will get total for each FK row and wil sum all
       
        return total


    @property 
    def get_cart_items(self):

        orderitems=self.orderitem_set.all() # so we went to child table get all order for this FK
        total=sum(item.quantity for item in orderitems) # it will call the quanitity for each FK row and wil sum all
       
        return total
      





class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property 
    def get_total(self):
        total=self.product.price*self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address








