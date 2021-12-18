from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.

class Car(models.Model):
  
  city_choice = (
    ('Alexandria', 'Alexandria'),
    ('Aswan', 'Aswan'),
    ('Asyut', 'Asyut'),
    ('Beheira', 'Beheira'),
    ('Beni Suef', 'Beni Suef'),
    ('Cairo', 'Cairo'),
    ('Dakahlia', 'Dakahlia'),
    ('Damietta', 'Damietta'),
    ('Fayoum', 'Fayoum'),
    ('Gharbia', 'Gharbia'),
    ('Giaz', 'Giza'),
    ('Ismailia', 'Ismailia'),
    ('Kafr al-Sheikh', 'Kafr al-Sheikh'),
    ('Luxor', 'Luxor'),
    ('Matruh', 'Matruh'),
    ('Minya', 'Minya'),
    ('Monufia', 'Monufia'),
    ('New Valley', 'New Valley'),
    ('Port Said', 'Port Said'),
    ('Qalyubia', 'Qalyubia'),
    ('Qena', 'Qena'),
    ('Red Sea', 'Red Sea'),
    ('Sharqia', 'Sharqia'),
    ('Sohag', 'Sohag'),
    ('South Sinai', 'South Sinai'),
    ('Suez', 'Suez'),
    
    
  )
  
  year_choice = []
  for r in range(1990, (datetime.now().year+1)):
    year_choice.append((r,r))
  
  features_choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audio Interface', 'Audio Interface'),
    ('Airbags', 'Airbags'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Seat Heating', 'Seat Heating'),
    ('Alarm System', 'Alarm System'),
    ('ParkAssist', 'ParkAssist'),
    ('Power Steering', 'Power Steering'),
    ('Reversing Camera', 'Reversing Camera'),
    ('Direct Fuel Injection', 'Direct Fuel Injection'),
    ('Auto Start/Stop', 'Auto Start/Stop'),
    ('Wind Deflector', 'Wind Deflector'),
    ('Bluetooth Handset', 'Bluetooth Handset'),
)

  door_choices = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)
  
  
  car_title = models.CharField(max_length=200)
  city = models.CharField(choices=city_choice, max_length=100)
  color = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  year = models.IntegerField(('year'), choices=year_choice)
  condition = models.CharField(max_length=100)
  price = models.IntegerField()
  description = RichTextField()
  car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  features = MultiSelectField(choices=features_choices)
  body_style = models.CharField(max_length=100)
  engine = models.CharField(max_length=100)
  transmission = models.CharField(max_length=100)
  interior = models.CharField(max_length=50)
  kilometers = models.IntegerField()
  doors = models.CharField(choices=door_choices, max_length=10)
  passengers = models.IntegerField()
  vin_no = models.CharField(max_length=100)
  miles = models.IntegerField()
  fuel_type = models.CharField(max_length=50)
  no_of_owners = models.CharField(max_length=50)
  Warranty = models.CharField(max_length=100, blank=True)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now, blank=True)
  
  
  def __str__(self):
    return self.car_title
