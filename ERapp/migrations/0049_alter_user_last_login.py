# Generated by Django 4.2.5 on 2023-10-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0048_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]