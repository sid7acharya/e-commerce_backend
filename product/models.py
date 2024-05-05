from django.db import models
from user.models import user
from category.models import Category

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=100, blank=False, null=False)
    description=models.CharField(max_length=100, blank=False, null=False)
    price=models.FloatField(default=99)
    stock_quantity=models.IntegerField(default=1, null=True, blank=True)
    rating=models.IntegerField(default=4)
    image=models.ImageField(default='image_1926.JPG')
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None, null=True, blank=True)
    
    seller=models.ForeignKey(user, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.title
    


