from django.db import  models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone
from PIL import Image
import subprocess
import os

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class USER(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    profile_pic = models.ImageField(blank=True, upload_to='uploads/profilePic')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    user_id = models.CharField(max_length=255,blank=True, null=True)
    profile_pic = models.ImageField(blank=True,upload_to='uploads/profilePic')

   
    
    # Add any additional fields you need for your user model
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    





    


class ImageModel(models.Model):
    user_id = models.CharField(max_length=255)
    imageTitle =models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/profilePic')
    



    
class TableData001(models.Model):
    cell_id = models.CharField(max_length=255,blank=True)
    firstname = models.CharField(max_length=255,blank=True)
    lastname = models.CharField(max_length=255,blank=True)
    address = models.CharField(max_length=255,blank=True)
    num = models.CharField(max_length=255,blank=True)
    vt = models.FileField(upload_to='uploads/files',blank=True)
    etat = models.CharField(max_length=255,blank=True)
    tp = models.CharField(max_length=255,blank=True)
    auditV1 = models.FileField(upload_to='uploads/files/%Y/%m/%d/',blank=True)
    auditV2 = models.FileField(upload_to='uploads/files/%Y/%m/%d/',blank=True)
    auditV3 = models.FileField(upload_to='uploads/files/%Y/%m/%d/',blank=True)
    coffrac = models.CharField(max_length=255,blank=True)
    paiement = models.BooleanField(default=False)
    agent= models.CharField(max_length=255,blank=True)
    creation_time =models.DateTimeField(auto_now_add=True, blank = True)
    def __str__(self):
        return f'{self.cell_id} {self.firstname} {self.lastname}'
    
class file_table_auditV1(models.Model):
    
    file_index = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=255,blank=True)
    file_name = models.CharField(max_length=255,blank=True)
    file_save = models.FileField(upload_to=f'uploads/data/auditV1',blank=True ,unique=True)
    file_format = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f'{self.file_id} {self.file_index} {self.file_name}'
    
    

class file_table_auditV2(models.Model):
    
    file_index = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=255,blank=True)
    file_name = models.CharField(max_length=255,blank=True)
    file_save = models.FileField(upload_to=f'uploads/data/auditV2',blank=True ,unique=True)
    file_format = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f'{self.file_id} {self.file_index} {self.file_name}'
    
class file_table_auditV3(models.Model):
    
    file_index = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=255,blank=True)
    file_name = models.CharField(max_length=255,blank=True)
    file_save = models.FileField(upload_to=f'uploads/data/auditV3',blank=True ,unique=True)
    file_format = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f'{self.file_id} {self.file_index} {self.file_name}'
class file_table_auditFinal(models.Model):
    
    file_index = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=255,blank=True)
    file_name = models.CharField(max_length=255,blank=True)
    file_save = models.FileField(upload_to=f'uploads/data/auditFinal',blank=True ,unique=True)
    file_format = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f'{self.file_id} {self.file_index} {self.file_name}'
class file_table_vt(models.Model):
    
    file_index = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=255,blank=True)
    file_name = models.CharField(max_length=255,blank=True)
    file_save = models.FileField(upload_to=f'uploads/data/vt',blank=True ,unique=True)
    file_format = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return f'{self.file_id} {self.file_index} {self.file_name}'
    
    
class message_box_1(models.Model):
    message_id= models.CharField(max_length=255,blank=True)
    user_id = models.CharField(max_length=255,blank=True)
    row_id = models.CharField(max_length=255,blank=True)
    username = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,blank=True)
    message = models.CharField(max_length=255,blank=True)
    message_date = models.DateTimeField(default=timezone.now)
    box = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return f'{self.email} {self.message}'