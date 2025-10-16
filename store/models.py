from django.db import models


class Meds(models.Model):
    name = models.CharField(max_length=60 , blank = False ,null = False)
    image = models.ImageField(upload_to='images', blank = False , null  = False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.IntegerField()
    in_cart = models.BooleanField(default= False)  
    
    def __str__(self):
         return self.name 
    class Meta:
        verbose_name_plural = "Meds"


    
