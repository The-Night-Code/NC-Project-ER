# Generated by Django 4.2.5 on 2023-09-29 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0033_tabledata001_vt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabledata001',
            name='vt',
        ),
    ]
