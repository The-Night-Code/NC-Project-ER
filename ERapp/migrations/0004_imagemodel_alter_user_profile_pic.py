# Generated by Django 4.2.5 on 2023-09-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0003_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/profilePic')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='uploads/profilePic'),
        ),
    ]
