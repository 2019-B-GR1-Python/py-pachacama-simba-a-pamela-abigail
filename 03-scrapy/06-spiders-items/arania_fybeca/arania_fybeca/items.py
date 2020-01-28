# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    
class AraniaFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
