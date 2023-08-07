from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ] 
    def __str__(self):
        return self.title +' ' + self.author
    




class GenderChoices(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'

class Author(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.OTHER)
    def __str__(self):
        return self.Name

    
class Category(models.Model):
    title = models.CharField(max_length=255)
    countatni = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author,on_delete=models.PROTECT,default= 1)
    def __str__(self):
        return self.title

class Items(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inverntory = models.SmallIntegerField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default= 4)
    def __str__(self):
        return self.title
    # author = models.ForeignKey(Author,on_delete=models.PROTECT,default= 1)
    







