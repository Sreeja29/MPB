from django.db import models

# Create your models here.

CUSTOMER_CHOICES = [
    ("JEWELRY",'jewelry'),
    ("LAND", 'land'),
    ("VEHICLES",'vehicles'),
]

class Customer(models.Model):
    redgid=models.IntegerField()
    contactnumber=models.BigIntegerField()
    name=models.CharField(max_length=50)
    cust=models.CharField(max_length=100, choices=CUSTOMER_CHOICES)
    def __str__(self):
        return self.name
