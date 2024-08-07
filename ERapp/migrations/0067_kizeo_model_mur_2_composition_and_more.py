# Generated by Django 4.2.5 on 2023-10-12 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0066_kizeo_model_kizeo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Composition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Date_d_isolation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Epaisseur_isolant',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Epaisseur_mur',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Isolation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Photo_mur',
            field=models.ImageField(blank=True, default='uploads/data/kizeo/blank-white.jpg', upload_to='uploads/data/kizeo'),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Mur_2_Preuve_d_isolation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
