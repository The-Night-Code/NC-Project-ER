# Generated by Django 4.2.5 on 2023-10-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0115_activities_audit_activity_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities_audit',
            name='Activity_delete',
            field=models.BooleanField(default=False),
        ),
    ]