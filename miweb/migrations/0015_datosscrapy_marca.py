# Generated by Django 3.0.8 on 2021-04-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0014_datosscrapy_denominacion_de_origen'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosscrapy',
            name='marca',
            field=models.CharField(default='hola', max_length=255),
            preserve_default=False,
        ),
    ]
