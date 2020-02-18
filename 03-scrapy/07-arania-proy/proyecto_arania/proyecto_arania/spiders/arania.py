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
    name = 'cinecalidad' #
    allowed_domains = [
        'cinecalidad.to'
    ]
    start_urls = [
        'https://www.cinecalidad.to'
    ]
    
    regla_uno = ( 
        Rule(LinkExtractor(), callback= 'parse_page')
        ,
    )
    # busque en un link especifico con partes d ela url, segmentos de busqeuda
    url_segmento_permitido = ( # busque en un sitio especifico
        'genero-peliculas/accion',
        'genero-peliculas/infantil',
        'genero-peliculas/comedia',
        'genero-peliculas/terror',
        'genero-peliculas/ciencia-ficcion',
        'peliculas/2000',
        'peliculas/2001',
        'peliculas/2005',
        'peliculas/2010',
        'peliculas/2018',
        'peliculas/2019',
        'peliculas/2020',
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
        'genero-peliculas/romance',
        'genero-peliculas/drama',
        'genero-peliculas/crimen',
        'peliculas/2003',
        'peliculas/2004',
        'peliculas/2007',
        'peliculas/2008',
        'peliculas/2015',
        'peliculas/2014',
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
    
    
    rules = regla_dos

    def parse_page(self, response):
        titulo = response.css(
           'div.home_post_cont post_box > div > h3.hover_caption_caption > div.home_post_content > div.in_title :: text'
        ).extract()
        genero = response.css(
           'div.home_post_cont post_box > div > h3.hover_caption_caption > div.home_post_content > div.home_post_cat > a ::text'
        ).extract()
        detalle = response.css(
            'div.home_post_cont post_box > div > h3.hover_caption_caption > div.home_post_content > p::text'
        ).extract()
        imagen = response.css(
            'div.home_post_cont post_box > div > img ::attr(src)'
        ).extract()
        print(titulo,genero,detalle,imagen)

        exportar_csv(titulo,genero,detalle,imagen)

        for agencia in titulo:
            with open('onu_agencias.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')

