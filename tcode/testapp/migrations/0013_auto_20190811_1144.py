# Generated by Django 2.2.4 on 2019-08-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_auto_20190711_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='transpost',
            name='language_result',
            field=models.TextField(blank=True, null=True, verbose_name='번역결과'),
        ),
        migrations.AlterField(
            model_name='transpost',
            name='document',
            field=models.TextField(max_length=5000, verbose_name='번역할 문장'),
        ),
        migrations.AlterField(
            model_name='transpost',
            name='language',
            field=models.CharField(max_length=500, verbose_name='번역할 언어'),
        ),
    ]
