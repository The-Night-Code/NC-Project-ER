# Generated by Django 4.2.5 on 2023-10-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0043_tabledata001_paiement'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabledata001',
            name='agent',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
