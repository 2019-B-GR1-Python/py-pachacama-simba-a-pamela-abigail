import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


def exportar_csv(titulo,genero,detalle,imagen):
   import csv
   with open('shein.csv','a', newline='') as csvfile:
       spamwriter = csv.writer(csvfile, delimiter = ',')
       data = list(zip(titulo,genero,detalle,imagen))
       for row in data:
           row = list(row)
           spamwriter.writerow(row)

class AraniaCrawlPelis(CrawlSpider):
    name = 'novicompu' #
    allowed_domains = [
        'novicompu.com'
    ]
    start_urls = [
        'https://www.novicompu.com/'
    ]
    
    regla_uno = ( 
        Rule(LinkExtractor(), callback= 'parse_page')
        ,
    )
    # busque en un link especifico con partes d ela url, segmentos de busqeuda
    url_segmento_permitido = ( # busque en un sitio especifico
        '12-laptops-pcs-cpu',
        '7-celulares-tablets-smart-bands',
        '79-televisores',
        '110-impresoras-scanners',
        '78-audio-video',
        '169-entretenimiento',
    )
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page'
        ),
    )
    
    url_segmento_restringido = (
        '99-deportes',
        '100-hogar',
        '120-juguetes',
        '101-accesorios-para-vehiculos',
        '296-sillas-de-oficina',
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido,
               # deny=url_segmento_restringido
            ),callback='parse_page'
        ),
    )
    
    
    rules = regla_uno

    def parse_page(self, response):
        def precio_f(precio):
            return float(precio[1::])

        categorias = response.css(
           'div.container > div.row > div > div.addon-box > div.products > div.item > div > div.product-info > div.category-name > a::Text'
        ).extract()
        nombre= response.css(
            'div.container > div.row > div > div.addon-box > div.products > div.item > div > div.product-info > div.product-name > a::Text'
        ).extract()
        precio = response.css(
            'div.container > div.row > div > div.addon-box > div.products > div.item > div > div.product-info > div.div.content_price > span::Text'
        ).extract()
        imagen = response.css(
             'div.container > div.row > div > div.addon-box > div.products > div.item > div > div.preview > a > img.img-responsive::attr(data-src)'
        ).extract()
        
        print(titulo,genero,detalle,imagen)

        exportar_csv(titulo,genero,detalle,imagen)

        for agencia in titulo:
            with open('onu_agencias.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')

