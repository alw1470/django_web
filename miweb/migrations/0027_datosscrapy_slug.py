# Generated by Django 3.0.8 on 2021-04-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0026_remove_datosscrapy_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosscrapy',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
