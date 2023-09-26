from django.db import models

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

    
class TableData1(models.Model):
    cell_data = models.CharField(max_length=255)
    cell_data2 = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.cell_data}'
    

class ImageModel(models.Model):
    user_id = models.CharField(max_length=255)
    imageTitle =models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/profilePic')
    
class TableData(models.Model):
    cell_data = models.CharField(max_length=255)
    cell_data2 = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.cell_data}'



class TableData01(models.Model):
    cell_data = models.CharField(max_length=255, default=None, blank=True, null=True)
    cell_data2 = models.CharField(max_length=255, default=None, blank=True, null=True)
    cell_data3 = models.CharField(max_length=255, default=None, blank=True, null=True)
    cell_data4 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data5 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data6 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data7 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data8 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data9 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data10 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data11 = models.CharField(max_length=500, default=None, blank=True, null=True)
    cell_data12 = models.CharField(max_length=500, default=None, blank=True, null=True)
    

    
    def __str__(self):
        return f'{self.cell_data}'