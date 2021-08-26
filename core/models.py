from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Currency(models.Model):
    code =models.CharField(max_length=3,blank=True,unique=True)
    name = models.CharField(max_length=25,blank=True)

    def __str__(self):
        return f"{self.code}"
class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='categories')
    name = models.CharField(max_length=56,blank=True)

    def __str__(self):
        return f"{self.name}"
class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='transactions')
    amount =models.DecimalField(max_digits= 15,decimal_places=2)
    currency=models.ForeignKey(Currency,on_delete=models.PROTECT,related_name='transactions')
    date = models.DateField(default=timezone.now)
    description=models.TextField(blank=True)
    cataegory=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='transactions')

    def __str__(self):
        return f"{self.amount} ({self.currency.code}) ({self.date})"