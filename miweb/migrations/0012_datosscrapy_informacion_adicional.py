# Generated by Django 3.0.8 on 2021-04-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0011_auto_20210411_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosscrapy',
            name='informacion_adicional',
            field=models.CharField(default='hola', max_length=255),
            preserve_default=False,
        ),
    ]
