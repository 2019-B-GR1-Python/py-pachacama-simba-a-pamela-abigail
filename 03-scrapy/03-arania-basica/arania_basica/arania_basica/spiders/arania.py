import scrapy

def guardar_datos(titulo, precio, imagen):
    import csv
    with open('datos.csv','ab',) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulo, precio, imagen))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)
    print("creado")

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider' 
    urls = ['http://books.toscrape.com/index.html']
    lista_categorias=[]
    bandera = False

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        def precio_f(precio):
            return float(precio[1::])
        
        if(self.bandera == False):
            etiqueta_contenedora= response.css('div.side_categories')
            categorias =etiqueta_contenedora.css(' ul > li > ul > li > a::attr(href)').extract()
            print(categorias)
            self.lista_categorias.append("http://books.toscrape.com/"+ categorias[0])
            for p in categorias[1:]:
                p =  "http://books.toscrape.com/"+p
                self.lista_categorias.append(p)
            print(self.lista_categorias)
            for p in self.lista_categorias[1:]:
                yield scrapy.Request(p, callback=self.parse)
                self.bandera = True
        else:
            etiqueta_contenedora = response.css('article.product_pod')
            titulos = etiqueta_contenedora.css('h3 > a::text').extract()
            precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
            precio_float= list(map(precio_f, precios))
            imagenes = etiqueta_contenedora.css('div.image_container > a > img ::attr(src)').extract()
            lista_imagenes=[]
            for p in imagenes:
                p = "http://books.toscrape.com"+p[11:]
                lista_imagenes.append(p)

            print(titulos)
            print(lista_imagenes)
            print(precio_float)
            guardar_datos(titulos, precio_float, lista_imagenes)
            
            

               





     

