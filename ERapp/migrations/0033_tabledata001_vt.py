# Generated by Django 4.2.5 on 2023-09-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0032_remove_tabledata001_vt'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabledata001',
            name='vt',
            field=models.FileField(blank=True, upload_to='uploads/files'),
        ),
    ]
