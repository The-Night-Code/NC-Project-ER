# Generated by Django 4.2.5 on 2023-10-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0088_kizeo_model_saisie_par_piece_signature_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kizeo_model',
            name='Porte_1_Nombre',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='kizeo_model',
            name='Porte_2_Nombre',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]