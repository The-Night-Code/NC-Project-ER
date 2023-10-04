# Generated by Django 4.2.5 on 2023-10-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0041_file_table_auditv2_file_table_auditv3_file_table_vt'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_table_auditFinal',
            fields=[
                ('file_index', models.AutoField(primary_key=True, serialize=False)),
                ('file_id', models.CharField(blank=True, max_length=255)),
                ('file_name', models.CharField(blank=True, max_length=255)),
                ('file_save', models.FileField(blank=True, unique=True, upload_to='uploads/data/auditFinal')),
                ('file_format', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='file_table_auditv2',
            name='file_save',
            field=models.FileField(blank=True, unique=True, upload_to='uploads/data/auditV2'),
        ),
        migrations.AlterField(
            model_name='file_table_auditv3',
            name='file_save',
            field=models.FileField(blank=True, unique=True, upload_to='uploads/data/auditV3'),
        ),
        migrations.AlterField(
            model_name='file_table_vt',
            name='file_save',
            field=models.FileField(blank=True, unique=True, upload_to='uploads/data/vt'),
        ),
    ]
