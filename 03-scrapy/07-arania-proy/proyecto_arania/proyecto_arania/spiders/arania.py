import scrapy
class AraniaPrueba(scrapy.Spider):
    name = "arania_prueba"
    url_base = "https://www.espaebook.org/"
    urls = [
        "https://www.espaebook.org/"
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_categories_links) # yield--> Esperar para que se complete la linea (no sea asincrona)

    def parse_categories_links(self, response):
        # categorias_peliculas = response.css("div.bk.brdr10px.br1px.mgbot20px.pd10px > ul.icoscat.bold.clf.icos.fs14px.f_left_li.liabrdr10px > li > a::text").extract()
        categorias_peliculas = response.css("div.category.container.mt40.hidden-xs > div.row > div.col-sm-5.col-sm-offset-1 > ul > li > a::attr(href)").extract()
        def transformar_a_url(link_categoria_relativo): 
            return self.url_base + link_categoria_relativo 
        if (categorias_peliculas):
            self.urls = list(map(transformar_a_url, categorias_peliculas))
            for url in self.urls:
                yield scrapy.Request(url=url, callback=self.parse_peliculas_all_links)

    def parse_peliculas_all_links(self, response):
        # url_pelicula = response.css("ul.peliculas.clf.cntclsx4.f_left_li > li.peli_bx.br1px.brdr10px.ico_a > div.peli_img.p_relative > div.peli_img_img > a::attr(href)").extract()
        siguiente = response.css(" div.row.mt44.optionsBar > div.fr.pages::text").extract()
        def transformar_a_number(respuesta):
            return respuesta.rstrip().lstrip()[3:]
        paginas_categoria = list(map(transformar_a_number, siguiente))
        url_actual = response.request.url
        numero_paginas = int(paginas_categoria[2])
        for x in range(2,numero_paginas+1):
            self.urls.append(url_actual + "/" +str(x))
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_info_peliculas)

    def parse_info_peliculas(self, response):
        titulo = response.css("div.row.laText > div.col-sm-20.mt10 > h3.tlc > a.title::text").extract()
        autor_array = response.css("div.row.laText > div.col-sm-20.mt10 > div.row.mt10 > div.col-sm-10.padIt > a::text").extract()
        publicado = response.css("div.row.laText > div.col-sm-20.mt10 > div.row.mt10 > div.col-sm-10.hidden-xs.padIt > b::text").extract()
        autor = autor_array[::2]
        categoria = autor_array[1::2] # categotia
        fecha_publicado = publicado[::3]
        num_descargas = publicado[1::3] ## descargas
        num_paginas = publicado[2::3] ## num paginas
        guardar_archivo(titulo, autor, categoria, fecha_publicado, num_descargas, num_paginas)

def guardar_archivo(titulo, autor, categoria, fecha_publicado, num_descargas, num_paginas):
    import csv
    with open('libros.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulo, autor, categoria, fecha_publicado, num_descargas, num_paginas))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)