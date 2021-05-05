# Generated by Django 3.0.8 on 2021-05-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspador', '0002_categoriasdatosscrapy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriasdatosscrapy',
            name='texto',
        ),
        migrations.AddField(
            model_name='categoriasdatosscrapy',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='categoriasdatosscrapy',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]