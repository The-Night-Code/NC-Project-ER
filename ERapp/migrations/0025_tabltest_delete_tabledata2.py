# Generated by Django 4.2.5 on 2023-09-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0024_alter_tabledata2_cell_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_data', models.CharField(max_length=255)),
                ('cell_data2', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='TableData2',
        ),
    ]
