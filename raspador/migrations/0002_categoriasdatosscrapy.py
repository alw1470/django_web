# Generated by Django 3.0.8 on 2021-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasDatosScrapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True)),
            ],
        ),
    ]