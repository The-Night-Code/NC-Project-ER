# Generated by Django 4.2.5 on 2023-12-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0128_userstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_box_1',
            name='user_Vue',
            field=models.TextField(blank=True),
        ),
    ]