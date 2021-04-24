from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import  RichTextField
from scrapy_djangoitem import DjangoItem


class DatosScrapy(models.Model):
    texto = models.TextField(blank=True)