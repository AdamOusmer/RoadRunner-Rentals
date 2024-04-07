from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_license = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_license_plate = models.CharField(max_length=10)
    car_VIN = models.CharField(max_length=17)
    car_color = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='car_images', null=True)


class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)
    branch_city = models.CharField(max_length=50)
    branch_province = models.CharField(max_length=50)
    branch_zip = models.CharField(max_length=6)
    branch_country = models.CharField(max_length=50)


class Rental(models.Model):
    rental_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    rental_start_date = models.DateTimeField()
    rental_end_date = models.DateTimeField()
    rental_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
