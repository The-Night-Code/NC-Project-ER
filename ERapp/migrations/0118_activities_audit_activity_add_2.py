# Generated by Django 4.2.5 on 2023-11-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0117_rename_ai_or_agent_name_ai_or_agent_comp_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities_audit',
            name='Activity_add_2',
            field=models.BooleanField(default=False),
        ),
    ]