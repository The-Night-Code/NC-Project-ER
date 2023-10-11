# Generated by Django 4.2.5 on 2023-10-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0058_mymodel_image_field_2_mymodel_image_field_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='kizeo_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facade_1_Orientation', models.CharField(blank=True, max_length=100)),
                ('Facade_1_Mitoyennete', models.CharField(blank=True, max_length=100)),
                ('Facade_1_Longueur', models.FloatField()),
                ('Facade_1_Hauteur', models.FloatField()),
                ('Facade_1_Surface', models.FloatField()),
                ('Facade_1_Photo_Principale', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Facade_2_Orientation', models.CharField(blank=True, max_length=100)),
                ('Facade_2_Mitoyennete', models.CharField(blank=True, max_length=100)),
                ('Facade_2_Longueur', models.FloatField()),
                ('Facade_2_Hauteur', models.FloatField()),
                ('Facade_2_Surface', models.FloatField()),
                ('Facade_2_Photo_Principale', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Facade_3_Orientation', models.CharField(blank=True, max_length=100)),
                ('Facade_3_Mitoyennete', models.CharField(blank=True, max_length=100)),
                ('Facade_3_Longueur', models.FloatField()),
                ('Facade_3_Hauteur', models.FloatField()),
                ('Facade_3_Surface', models.FloatField()),
                ('Facade_3_Photo_Principale', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Facade_4_Orientation', models.CharField(blank=True, max_length=100)),
                ('Facade_4_Mitoyennete', models.CharField(blank=True, max_length=100)),
                ('Facade_4_Longueur', models.FloatField()),
                ('Facade_4_Hauteur', models.FloatField()),
                ('Facade_4_Surface', models.FloatField()),
                ('Facade_4_Photo_Principale', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Cauffage_systeme', models.CharField(blank=True, max_length=100)),
                ('Cauffage_annee_de_mise_en_oeuvre', models.IntegerField()),
                ('Cauffage_photo_systeme_de_production', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Cauffage_photo_fiche_signaletique', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Cauffage_type_de_regulation', models.CharField(blank=True, max_length=100)),
                ('Cauffage_system_d_appoint', models.CharField(blank=True, max_length=100)),
                ('Cauffage_photo_appoint', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Cauffage_commentaire', models.CharField(blank=True, max_length=750)),
                ('ECS_system_d_appoint', models.CharField(blank=True, max_length=100)),
                ('ECS_photo_appoint', models.ImageField(upload_to='uploads/data/kizeo')),
                ('ECS_commentaire', models.CharField(blank=True, max_length=750)),
                ('ECS_type', models.CharField(blank=True, max_length=100)),
                ('Ventilation_photo_ventilation', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Refroidissement_type', models.CharField(blank=True, max_length=100)),
                ('Refroidissement_commentaire', models.CharField(blank=True, max_length=750)),
                ('Compteur_Electrique_Puissance_souscrite', models.FloatField()),
                ('Compteur_Electrique_type', models.CharField(blank=True, max_length=100)),
                ('Compteur_Electrique_photo_compteur', models.ImageField(upload_to='uploads/data/kizeo')),
                ('Compteur_Electrique_commentaire', models.CharField(blank=True, max_length=750)),
            ],
        ),
    ]
