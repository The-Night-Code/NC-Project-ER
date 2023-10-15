# Generated by Django 4.2.5 on 2023-10-08 21:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0050_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_box_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(blank=True, max_length=255)),
                ('user_id', models.CharField(blank=True, max_length=255)),
                ('row_id', models.CharField(blank=True, max_length=255)),
                ('username', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('message', models.CharField(blank=True, max_length=255)),
                ('message_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]