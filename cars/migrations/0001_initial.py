# Generated by Django 3.0.7 on 2021-12-14 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('Aswan', 'Aswan'), ('Asyut', 'Asyut'), ('Beheira', 'Beheira'), ('Beni Suef', 'Beni Suef'), ('Cairo', 'Cairo'), ('Dakahlia', 'Dakahlia'), ('Damietta', 'Damietta'), ('Fayoum', 'Fayoum'), ('Gharbia', 'Gharbia'), ('Giaz', 'Giza'), ('Ismailia', 'Ismailia'), ('Kafr al-Sheikh', 'Kafr al-Sheikh'), ('Luxor', 'Luxor'), ('Matruh', 'Matruh'), ('Minya', 'Minya'), ('Monufia', 'Monufia'), ('New Valley', 'New Valley'), ('Port Said', 'Port Said'), ('Qalyubia', 'Qalyubia'), ('Qena', 'Qena'), ('Red Sea', 'Red Sea'), ('Sharqia', 'Sharqia'), ('Sohag', 'Sohag'), ('South Sinai', 'South Sinai'), ('Suez', 'Suez')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=550)),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=100)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('interior', models.CharField(max_length=50)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=50)),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=100)),
                ('no_of_owners', models.CharField(max_length=50)),
                ('if_featured', models.BooleanField(max_length=50)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
