# Generated by Django 4.2.5 on 2023-10-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0051_message_box_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_box_1',
            name='box',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
