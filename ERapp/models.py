from django.db import models

# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=320)

    
