import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider' 
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        def precio_f(precio):
            return float(precio[1::])


        #etiqueta_contenedora = response.css('article.product_pod')
        #titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        #precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        #precio_float= list(map(precio_f, precios))
        #imagenes = etiqueta_contenedora.css('div.image_container > a > img ::attr(src)').extract()
        etiqueta_contenedora2= response.css('div.side_categories')
        categorias =etiqueta_contenedora2.css(' ul > li > ul > li > a::attr(href)').extract()

        #print(titulos)
        #print(imagenes)
        #print(precio_float)
        print(categorias)