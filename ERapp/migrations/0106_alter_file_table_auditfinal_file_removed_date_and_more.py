# Generated by Django 4.2.5 on 2023-10-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERapp', '0105_rename_file_removed_user_file_table_auditfinal_file_removed_user_fn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_table_auditfinal',
            name='file_removed_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='file_table_auditv1',
            name='file_removed_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='file_table_auditv2',
            name='file_removed_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='file_table_auditv3',
            name='file_removed_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]