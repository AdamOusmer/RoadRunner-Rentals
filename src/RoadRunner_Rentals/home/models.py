from django.db import models

# Create your models here.


class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_license_plate = models.CharField(max_length=10)
    car_VIN = models.CharField(max_length=17)
    car_color = models.CharField(max_length=50)


class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)
    branch_city = models.CharField(max_length=50)
    branch_province = models.CharField(max_length=50)
    branch_zip = models.CharField(max_length=6)
    branch_country = models.CharField(max_length=50)