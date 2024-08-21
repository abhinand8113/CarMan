from django.db import models
from django.utils.timezone import datetime
from datetime import date

# Create your models here.
class driver_reg(models.Model):
    DriverId=models.CharField(max_length=30)
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Email=models.EmailField()
    State=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Password=models.CharField(max_length=30)
    Cnf_password=models.CharField(max_length=30)
    Licence=models.FileField()
    Zip=models.IntegerField()
    Status=models.CharField(max_length=30)

    def __str__(self):
        return self.Username

class driver_login(models.Model):
    Username=models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    def __str__(self):
        return self.Username

class user_reg(models.Model):
    UserId=models.CharField(max_length=30)
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Password=models.CharField(max_length=30)
    Cnf_password=models.CharField(max_length=30)
    def __str__(self):
        return self.Username

class user_login(models.Model):
    Username=models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    def __str__(self):
        return self.Username

#################################################################################

class one_way(models.Model):
    Name=models.CharField(max_length=30)
    Date=models.CharField(max_length=30)
    StartingL=models.CharField(max_length=30)
    EndingL=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Type=models.CharField(max_length=30)
    def __str__(self):
        return self.Name

class round_trip(models.Model):
    Name=models.CharField(max_length=30)
    Date=models.CharField(max_length=30)
    StartingL = models.CharField(max_length=30)
    EndingL = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Type=models.CharField(max_length=30)
    def __str__(self):
        return self.Name

class package(models.Model):
    Name= models.CharField(max_length=30)
    Destination=models.CharField(max_length=30)
    StartingL = models.CharField(max_length=30)
    S_date=models.CharField(max_length=30)
    E_date=models.CharField(max_length=30)
    Days = models.IntegerField()
    Phone = models.IntegerField()
    Type=models.CharField(max_length=30)
    Payment_status=models.CharField(max_length=20)
    def __str__(self):
        return self.Name

#################################################################################

class admin_login(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    def __str__(self):
        return self.Username

class drivertableshow(models.Model):
    Name=models.CharField(max_length=30)
    Starting=models.CharField(max_length=30)
    Ending=models.CharField(max_length=30)
    Date=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Type=models.CharField(max_length=30)
    Status=models.CharField(max_length=30)
    DriverId=models.CharField(max_length=30)
    UserId=models.CharField(max_length=30)
    def __str__(self):
        return self.Name

class customer_message(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=50)
    Message=models.CharField(max_length=1000)
    def __str__(self):
        return self.Name


