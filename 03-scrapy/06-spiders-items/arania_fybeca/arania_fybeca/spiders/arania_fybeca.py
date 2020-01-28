# arania_fybeca.py
import scrapy
from arania_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaFybeca(scrapy.Spider):
    name = 'fybeca'
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
    ]

    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url = url)

    def parse(self, response):
        productos = request.css('div.product-title-inner')
        for producto in productos:
            detalle = producto.css('div.detail')
            tiene_detalle = len(detalle) > 0
            if(tiene_detalle):
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                producto_loader.default_output_processor=TakeFirst()
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )
                yield producto_loader.load_item()
    