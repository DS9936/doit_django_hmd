from django.db import models

# Create your models here.

class Ramen(models.Model):
    date = models.DateField()
    product_name = models.CharField(max_length=10)
    shinramyun = models.IntegerField()
    samyangramyun = models.IntegerField()
    jinramyun = models.IntegerField()
    average = models.IntegerField()
    
