# Scrapy 

## Instalación 

Se utiliza el siguiente comando en `Anaconda Prompt` 

``` 

pip install scrapy 

conda install -c conda-forge scrapy  

``` 

o una alternativa es 

``` 

conda install -c conda-forge scrapy  

``` 

## Comandos Generales 

* `scrapy bench` .- Da las caracteristicas para poder hacer web scraping o web crawling de ese computador 

* `scrapy settings`. - Visualizar las configuraciones extra 

* `scrapy version`. - Visualizar la version de Scrapy 

### scarpy view 'url'
´´´
$ scrapy view https://www.pluralsight.com/authors
´´´

no se ve contenido
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scarpy shell `url`


Permite `interactuar con la respuesta` del scrapy
$ scrapy shell http://quotes.toscrape.com/

$ response.css ('.title')
$ response.css ('.title').extract()
$ response.css ('.title::text').extract()
$ response.css ('.authors').extract()
$ response.css ('.authors::text').extract()
$ type(response.css ('.authors::text').extract())
$ response.css ('.authors::text').extract()[0]
$ response.css ('.authors::text')[0]
$ type(response.css ('.authors::text')[0])
$ response.css ('.authors::text')[0].extract()
$ response.css ('.authors::text').extract_first()
$ response.css ('span.text').extract()
$ response.css ('span.text::text').extract()
$ response.css ('.tag::text').extract()
$ response.css ('.tags > tag::text').extract()
$ response.css ('div.tags > a.tag::text').extract()
$ response.css ('.tags > tag::attr(href)').extract()
$ response.css ('div.quote> span > a ::attr(href)').extract()

NASA
$ response.css ('div.bg-card-canvas> div.headline ::attr(href)').extract()

XPATH
$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract() 
$ response.xpath('/html/body/div/div[2]/div[1]').extract()
$ response.xpath('/html/body/div/div[2]/div[1]/text()').extract()
$ response.xpath("//div [@class = 'quote']").extract()
$ response.xpath("//div [@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div [@class = 'quote']/span[@class='text']/text()").extract_first()
$ response.xpath("//div [@class = 'quote']/span/a/@href").extract_first()

## scrapy startproject arania-basica




