# Generated by Django 3.0.8 on 2021-04-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0003_auto_20210409_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosScrapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True)),
            ],
        ),
    ]