from django.db import models

# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=320)

    
class TableData1(models.Model):
    cell_data = models.CharField(max_length=255)
    cell_data2 = models.CharField(max_length=255)