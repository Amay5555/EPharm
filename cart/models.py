from django.db import models
from accounts.models import UserProfile
from store.models import Meds

class Cart(models.Model):
    user = models.OneToOneField(UserProfile , on_delete=models.CASCADE , null= True , blank= True)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Meds , on_delete=models.SET_NULL , null=True)
    quantity = models.PositiveIntegerField(default=1)