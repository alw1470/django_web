# Generated by Django 3.0.8 on 2021-04-09 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0005_datosscrapy_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosscrapy',
            name='body',
        ),
    ]
