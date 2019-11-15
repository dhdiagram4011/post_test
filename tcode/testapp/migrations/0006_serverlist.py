# Generated by Django 2.2.2 on 2019-07-01 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_transpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serverlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('team', models.CharField(max_length=500)),
                ('server_count', models.CharField(max_length=500)),
                ('model_name', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=500)),
                ('use_case', models.TextField(max_length=5000)),
            ],
        ),
    ]