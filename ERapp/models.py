from django.db import models
from django.utils import timezone
from PIL import Image
import subprocess
import os

# Create your models here.


class USER(models.Model):
    user_id = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=320)
    #profile_pic = models.ImageField(upload_to='uploads/profilePic')
    profile_pic = models.ImageField(blank=True,upload_to='uploads/profilePic')
    
    def __str__(self):
        return f'{self.username}'

    


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
    