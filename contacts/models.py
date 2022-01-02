from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
# Create your models here.

class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  car_id = models.IntegerField()
  customer_need = models.CharField(max_length=100)
  car_title = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=50)
  message = models.TextField(blank=True)
  user_id = models.IntegerField(blank=True)
  create_date = models.DateTimeField(blank=True, default=datetime.now)
  
  def __str__(self):
    return self.email