from django.db import models
from product.models import Product
from user.models import user

# Create your models here.

class Cart(models.Model):
    product=models.ManyToManyField(Product)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,default=1)
    
    def __str__(self):
        return self.product