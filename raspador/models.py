from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import  RichTextField
from scrapy_djangoitem import DjangoItem


class DatosScrapy(models.Model):
    texto = models.TextField(blank=True)

class CategoriasDatosScrapy(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=255, null=True,
                            blank=False, unique=True)
    def __str__(self):
        return self.title 