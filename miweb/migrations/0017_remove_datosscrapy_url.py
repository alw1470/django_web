# Generated by Django 3.0.8 on 2021-04-21 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0016_datosscrapy_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosscrapy',
            name='url',
        ),
    ]
