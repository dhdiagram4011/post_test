# Generated by Django 2.2.2 on 2019-06-27 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_reg_created_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reg',
            new_name='Post',
        ),
    ]
