# Generated by Django 3.0.8 on 2021-04-21 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0020_auto_20210421_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datosscrapy',
            old_name='url',
            new_name='url_2',
        ),
    ]