# Generated by Django 4.2.5 on 2023-10-23 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0087_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='kizeo_model',
            name='Saisie_par_piece_Signature_client',
            field=models.ImageField(blank=True, default='uploads/data/kizeo/blank-white.jpg', upload_to='uploads/data/kizeo'),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Saisie_par_piece_Signature_intervenant',
            field=models.ImageField(blank=True, default='uploads/data/kizeo/blank-white.jpg', upload_to='uploads/data/kizeo'),
        ),
        migrations.AddField(
            model_name='kizeo_model',
            name='Saisie_par_piece_Surface_Mesuree',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
