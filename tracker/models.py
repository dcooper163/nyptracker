from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ticket(models.Model):
    status = models.CharField(max_length=200)    
    number = models.CharField(max_length=200)
    assigned = models.CharField(max_length=200)
    def __str__(self):
        return self.number

class Customer(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    cwid = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    update = models.CharField(max_length=200)
    def __str__(self):
        return self.cwid