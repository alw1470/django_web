# Generated by Django 3.0.8 on 2021-04-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_review_product',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
