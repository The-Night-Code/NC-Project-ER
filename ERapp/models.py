from django.db import  models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone
from PIL import Image
import subprocess
import os
import datetime
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
    agent = models.CharField(max_length=30, blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    profile_pic = models.ImageField(blank=True, upload_to='uploads/profilePic',default='uploads/default_user_avatar.png')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    user_id = models.CharField(max_length=255,blank=True, null=True)
    

   
    
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
    etat_vt = models.CharField(max_length=255,blank=True)
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
    
    
    
from django.db import models

class MyModel(models.Model):
    text_field = models.CharField(max_length=100,blank=True)
    image_field = models.ImageField(upload_to='images/')
    image_field_2 = models.ImageField(upload_to='images/',blank=True)
    image_field_3 = models.ImageField(upload_to='images/',blank=True)
    
class UpdatedXLSXFile(models.Model):
    name = models.CharField(max_length=100,blank=True)
    xlsx_file = models.ImageField(upload_to='uploads/data/kizeo')
    
    
class kizeo_model(models.Model):
    kizeo_id = models.CharField(max_length=100,blank=True)
    
    
    ### Données Générales
    latitude = models.CharField(max_length=100,blank=True)
    longitude = models.CharField(max_length=100,blank=True)
    altitude = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Nom_d_intervenant = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Date_de_visite = models.DateField(null=True,blank=True,default=datetime.date.today)
    Donnees_Generales_Adresse = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Zip_Code = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_City = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Annee_de_construction = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Etat_d_occupation = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Nom_client = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Tel_client = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_Email = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Horaire_d_occupation_des_lieux = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Destination_du_lieu = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Nombre_d_occupant = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_Nombre_de_niveau = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_Surface_TOTALE = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_Preuve_Surface = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Preuve_Surface_Photo = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/db/blank-white.jpg")
    Donnees_Generales_Surface_ajoute_depuis_moins_de_15_ans = models.IntegerField(default=0,null=True,blank=True)
    Donnees_Generales_Factures = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/db/blank-white.jpg")
    Donnees_Generales_Besoin_du_client_Chauffage = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Besoin_du_client_Isolation = models.CharField(max_length=100,blank=True)
    Donnees_Generales_Scenario_souhaite_par_le_client = models.CharField(max_length=100,blank=True)
    
    
    ### Façades
    Facade_1_Orientation =models.CharField(max_length=100,blank=True)
    Facade_1_Mitoyennete=models.CharField(max_length=100,blank=True)
    Facade_1_Longueur=models.FloatField(default=0.0,blank=True)
    Facade_1_Hauteur=models.FloatField(default=0.0,blank=True)
    Facade_1_Surface=models.FloatField(default=0.0,blank=True)
    Facade_1_Photo_Principale=models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    Facade_2_Orientation =models.CharField(max_length=100,blank=True)
    Facade_2_Mitoyennete=models.CharField(max_length=100,blank=True)
    Facade_2_Longueur=models.FloatField(default=0.0,blank=True)
    Facade_2_Hauteur=models.FloatField(default=0.0,blank=True)
    Facade_2_Surface=models.FloatField(default=0.0,blank=True)
    Facade_2_Photo_Principale=models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    Facade_3_Orientation =models.CharField(max_length=100,blank=True)
    Facade_3_Mitoyennete=models.CharField(max_length=100,blank=True)
    Facade_3_Longueur=models.FloatField(default=0.0,blank=True)
    Facade_3_Hauteur=models.FloatField(default=0.0,blank=True)
    Facade_3_Surface=models.FloatField(default=0.0,blank=True)
    Facade_3_Photo_Principale=models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    Facade_4_Orientation =models.CharField(max_length=100,blank=True)
    Facade_4_Mitoyennete=models.CharField(max_length=100,blank=True)
    Facade_4_Longueur=models.FloatField(default=0.0,blank=True)
    Facade_4_Hauteur=models.FloatField(default=0.0,blank=True)
    Facade_4_Surface=models.FloatField(default=0.0,blank=True)
    Facade_4_Photo_Principale=models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Cauffage
    Cauffage_systeme = models.CharField(max_length=100,blank=True)
    Cauffage_annee_de_mise_en_oeuvre = models.IntegerField(default=0,blank=True)
    Cauffage_photo_systeme_de_production = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Cauffage_photo_fiche_signaletique = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Cauffage_type_de_regulation = models.CharField(max_length=100,blank=True)
    Cauffage_system_d_appoint = models.CharField(max_length=100,blank=True)
    Cauffage_photo_appoint = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Cauffage_commentaire = models.CharField(max_length=750,blank=True)
    
    ### ECS
    ECS_type = models.CharField(max_length=100,blank=True)
    ECS_system_d_appoint = models.CharField(max_length=100,blank=True)
    ECS_photo_appoint = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    ECS_commentaire = models.CharField(max_length=750,blank=True)
    
    ### Ventilation
    Ventilation_type = models.CharField(max_length=100,blank=True)
    Ventilation_photo_ventilation = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Refroidissement
    Refroidissement_type = models.CharField(max_length=100,blank=True)
    Refroidissement_commentaire = models.CharField(max_length=750,blank=True)
    
    ### Compteur Electrique
    Compteur_Electrique_Puissance_souscrite = models.FloatField(default=0.0,blank=True)
    Compteur_Electrique_type = models.CharField(max_length=100,blank=True)
    Compteur_Electrique_photo_compteur = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Compteur_Electrique_commentaire = models.CharField(max_length=750,blank=True)
    
    ### Mur 1
    Mur_1_Position = models.CharField(max_length=100,blank=True)
    Mur_1_Composition = models.CharField(max_length=100,blank=True)
    Mur_1_Epaisseur_mur = models.IntegerField(default=0,blank=True)
    Mur_1_Isolation = models.CharField(max_length=100,blank=True)
    Mur_1_Epaisseur_isolant = models.IntegerField(default=0,blank=True)
    Mur_1_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Mur_1_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Mur_1_Photo_mur = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Mur 2
    Mur_2_Position = models.CharField(max_length=100,blank=True)
    Mur_2_Composition = models.CharField(max_length=100,blank=True)
    Mur_2_Epaisseur_mur = models.IntegerField(default=0,blank=True)
    Mur_2_Isolation = models.CharField(max_length=100,blank=True)
    Mur_2_Epaisseur_isolant = models.IntegerField(default=0,blank=True)
    Mur_2_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Mur_2_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Mur_2_Photo_mur = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Plancher bas 1
    Plancher_bas_1_Position = models.CharField(max_length=100,blank=True)
    Plancher_bas_1_Composition = models.CharField(max_length=100,blank=True)
    Plancher_bas_1_Surface = models.FloatField(default=0.0,blank=True)
    Plancher_bas_1_Isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_1_Epaisseur_isolant = models.FloatField(default=0.0,blank=True)
    Plancher_bas_1_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_1_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_1_Photo_plancher_bas = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Plancher bas 2
    Plancher_bas_2_Position = models.CharField(max_length=100,blank=True)
    Plancher_bas_2_Composition = models.CharField(max_length=100,blank=True)
    Plancher_bas_2_Surface = models.FloatField(default=0.0,blank=True)
    Plancher_bas_2_Isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_2_Epaisseur_isolant = models.FloatField(default=0.0,blank=True)
    Plancher_bas_2_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_2_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_bas_2_Photo_plancher_bas = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Plancher haut 1
    Plancher_Haut_1_Type = models.CharField(max_length=100,blank=True)
    Plancher_Haut_1_Composition = models.CharField(max_length=100,blank=True)
    Plancher_Haut_1_Surface = models.FloatField(default=0.0,blank=True)
    Plancher_Haut_1_Isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_1_Epaisseur_isolant = models.FloatField(default=0.0,blank=True)
    Plancher_Haut_1_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_1_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_1_Photo_plancher_bas = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Plancher haut 2
    Plancher_Haut_2_Type = models.CharField(max_length=100,blank=True)
    Plancher_Haut_2_Composition = models.CharField(max_length=100,blank=True)
    Plancher_Haut_2_Surface = models.FloatField(default=0.0,blank=True)
    Plancher_Haut_2_Isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_2_Epaisseur_isolant = models.FloatField(default=0.0,blank=True)
    Plancher_Haut_2_Date_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_2_Preuve_d_isolation = models.CharField(max_length=100,blank=True)
    Plancher_Haut_2_Photo_plancher_bas = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Fenetre type 1
    Fenetre_type_1_Menuiserie = models.CharField(max_length=100,blank=True)
    Fenetre_type_1_Materiaux = models.CharField(max_length=100,blank=True)
    Fenetre_type_1_Type_de_vitrage = models.CharField(max_length=100,blank=True)
    Fenetre_type_1_Volets = models.CharField(max_length=100,blank=True)
    Fenetre_type_1_Nombre = models.IntegerField(default=0,blank=True)
    Fenetre_type_1_Photo = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    ### Fenetre type 2
    Fenetre_type_2_Menuiserie = models.CharField(max_length=100,blank=True)
    Fenetre_type_2_Materiaux = models.CharField(max_length=100,blank=True)
    Fenetre_type_2_Type_de_vitrage = models.CharField(max_length=100,blank=True)
    Fenetre_type_2_Volets = models.CharField(max_length=100,blank=True)
    Fenetre_type_2_Nombre = models.IntegerField(default=0,blank=True)
    Fenetre_type_2_Photo = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    
    ### Porte 1
    Porte_1_Materiaux = models.CharField(max_length=100,blank=True)
    Porte_1_Type_porte = models.CharField(max_length=100,blank=True)
    Porte_1_Nombre = models.IntegerField(default=0,blank=True)
    Porte_1_Photo_porte = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
        
    ### Porte 2
    Porte_2_Materiaux = models.CharField(max_length=100,blank=True)
    Porte_2_Type_porte = models.CharField(max_length=100,blank=True)
    Porte_2_Nombre = models.IntegerField(default=0,blank=True)
    Porte_2_Photo_porte = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    
    signature_data = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Saisie_par_piece_Surface_Mesuree = models.FloatField(default=0.0,blank=True)
    Saisie_par_piece_Signature_intervenant = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    Saisie_par_piece_Signature_client = models.ImageField(upload_to='uploads/data/kizeo',blank=True,default="uploads/data/kizeo/blank-white.jpg")
    
    def __str__(self):
        return f'{self.kizeo_id} {self.Donnees_Generales_Nom_client}'
    
class kizeo_model_Pieces(models.Model):
    Pieces_index = models.AutoField(primary_key=True)
    kizeo_id = models.CharField(max_length=100,blank=True)
    Pieces_image_1 = models.ImageField(upload_to='uploads/data/kizeo',blank=True,null=True)
    Pieces_image_2 = models.ImageField(upload_to='uploads/data/kizeo',blank=True,null=True)
    Pieces_image_3 = models.ImageField(upload_to='uploads/data/kizeo',blank=True,null=True)
    Niveau = models.CharField(max_length=100,blank=True)

    Pieces = models.CharField(max_length=100,blank=True)
    Chauffage = models.CharField(max_length=100,blank=True)
    Mansardee = models.CharField(max_length=100,blank=True)
    HSP = models.FloatField(default=0.0,blank=True)
    
    Longueur = models.FloatField(default=0.0,blank=True)
    Largeur  = models.FloatField(default=0.0,blank=True)
    Surface = models.FloatField(default=0.0,blank=True)
    
    IF_mansardee= models.BooleanField(default=False) 
    HSF = models.FloatField(default=0.0,blank=True)
    HPP = models.FloatField(default=0.0,blank=True)
    LP = models.FloatField(default=0.0,blank=True)
    S_rampants_1 = models.FloatField(default=0.0,blank=True)
    S_rampants_2 = models.FloatField(default=0.0,blank=True)
    
    Decrochement_Longueur = models.FloatField(default=0.0,blank=True)
    Decrochement_Largeur  = models.FloatField(default=0.0,blank=True)
    Decrochement_Surface = models.FloatField(default=0.0,blank=True)
    
    Surface_nette = models.FloatField(default=0.0,blank=True)
    
    Menuiseries_F = models.CharField(max_length=1000,blank=True)
    Menuiseries_L = models.FloatField(default=0.0,blank=True)
    Menuiseries_H = models.FloatField(default=0.0,blank=True)
    Menuiseries_N = models.IntegerField(default=0,null=True,blank=True)
    
    def __str__(self):
        return f'{self.kizeo_id} {self.Pieces_index}'