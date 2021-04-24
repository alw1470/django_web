import uuid
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from scrapy_djangoitem import DjangoItem
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=False, null=False)
    title_review_product = models.CharField(max_length=255)
    #number_review_product = models.CharField(max_length=10)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class DatosScrapy(models.Model):
    title = models.CharField(max_length=255)
    precio_rebajado = models.CharField(max_length=255)
    precio_original = models.CharField(max_length=255)
    imagen = models.URLField()
    denominacion_de_origen = models.CharField(max_length=255)
    informacion_adicional = RichTextField(blank=False, null=False)
    marca = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True,
                            blank=False, unique=True)

    def __str__(self):
        return self.title + ' | ' + str(self.precio_original)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(DatosScrapy, self).save(*args, **kwargs)

# def set_slug(sender, instance, *args, **kwargs):
#     if instance.slug:
#         return
#         id = str(uuid.uuid4())
#         instance.slug = slugify('{}-{}'. format(
#             instance.title, id[:8]
#         ))


# pre_save.connect(set_slug, sender=DatosScrapy)
