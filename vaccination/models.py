from django.db import models

# Create your models here.

class registration(models.Model):
    user_name = models.CharField(max_length=200,null= False,blank =False)
    user_dob = models.DateField(null= False,blank =False)
    aadhar_number = models.BigIntegerField(primary_key=True,null= False,blank =False)
    phone_number = models.BigIntegerField(null= False,blank =False) 

class user(models.Model):
    register_number= models.CharField(max_length=150,primary_key=True,null= False,blank =False)
    first_dose = models.BooleanField(null=True)
    first_dose_place = models.CharField(max_length=100,null=True)
    first_dose_slot = models.CharField(max_length=100,null=True)
    first_dose_date = models.DateField(null=True)
    second_dose = models.BooleanField(null=True)
    second_dose_place = models.CharField(max_length=100,null=True)
    second_dose_slot = models.CharField(max_length=100,null=True)
    second_dose_date = models.DateField(null=True)
    user = models.ForeignKey(registration,on_delete=models.CASCADE)

class placeOne(models.Model):
    vaccination_date = models.DateField(primary_key=True,null= False,blank =False)
    slot_one = models.IntegerField(default=0)
    slot_two = models.IntegerField(default=0)
    slot_three = models.IntegerField(default=0)
    first_dose = models.IntegerField(default=0)
    second_dose = models.IntegerField(default=0)

class placeTwo(models.Model):
    vaccination_date = models.DateField(primary_key=True,null= False,blank =False)
    slot_one = models.IntegerField(default=0)
    slot_two = models.IntegerField(default=0)
    slot_three = models.IntegerField(default=0)
    first_dose = models.IntegerField(default=0)
    second_dose = models.IntegerField(default=0)

class placethree(models.Model):
    vaccination_date = models.DateField(primary_key=True,null= False,blank =False)
    slot_one = models.IntegerField(default=0)
    slot_two = models.IntegerField(default=0)
    slot_three = models.IntegerField(default=0)
    first_dose = models.IntegerField(default=0)
    second_dose = models.IntegerField(default=0)

class placeFour(models.Model):
    vaccination_date = models.DateField(primary_key=True,null= False,blank =False)
    slot_one = models.IntegerField(default=0)
    slot_two = models.IntegerField(default=0)
    slot_three = models.IntegerField(default=0)
    first_dose = models.IntegerField(default=0)
    second_dose = models.IntegerField(default=0)
