# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from miweb.models import Categorias
from miweb.models import DatosScrapy


class CategoriasItem(DjangoItem):
    django_model = Categorias

class DatosScrapyItem(DjangoItem):
    django_model = DatosScrapy
