# Generated by Django 3.0.8 on 2021-04-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0017_remove_datosscrapy_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosscrapy',
            name='url',
            field=models.SlugField(default='vinos', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
