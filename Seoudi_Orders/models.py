from django.db import models
from django.utils import timezone
# Create your models here.


class Order_Item(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 

class Customer(models.Model):
    name = models.CharField(max_length=225)
    Phone = models.IntegerField()
    def __str__(self):
        return self.name

class Order_Details(models.Model):
    CHOICES = (
        ('case1', '11'),
        ('case2', '22'),
        ('case3', '33'),
    )

    status = models.CharField(max_length=10, choices=CHOICES, default='option1')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default = None)
    Order_Number = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_after_Tax = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    # 
    flag = models.BooleanField(default=False)
    order_items = models.ManyToManyField(Order_Item)
    



