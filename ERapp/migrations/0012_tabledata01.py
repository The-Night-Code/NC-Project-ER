# Generated by Django 4.2.5 on 2023-09-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0011_alter_tabledata1_cell_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableData01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_data', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data2', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data3', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data4', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data5', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data6', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data7', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data8', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data9', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data10', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data11', models.CharField(blank=True, default=None, max_length=500)),
                ('cell_data12', models.CharField(blank=True, default=None, max_length=500)),
            ],
        ),
    ]
