# Generated by Django 4.2.8 on 2023-12-19 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_title_employee_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='boss',
            new_name='parent',
        ),
    ]
