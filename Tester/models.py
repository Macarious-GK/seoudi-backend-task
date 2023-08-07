from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 
    class Meta:   
        db_table = "Person" 
    def __str__(self): 
        return self.first_name 
    

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Person_Room(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    

class Desk_model(models.Model):
    status =models.CharField(max_length=255)
    Color =models.CharField(max_length=255)
    def __str__(self):
        return 'This is a ' + self.status +' Desk '+ 'and the color is: ' +self.Color
    
class Romes_Model_API(models.Model):
    Name = models.CharField(max_length=255)
    Area = models.DecimalField(decimal_places = 2,max_digits = 6)
    No_Beds = models.IntegerField()
    Desk = models.ForeignKey(Desk_model,on_delete=models.PROTECT,default=3)
    person = models.ForeignKey(Person_Room,on_delete=models.PROTECT,default=1)
    def __str__(self):
        return self.Name
    

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()



