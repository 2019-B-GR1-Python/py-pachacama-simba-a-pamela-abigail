
from scrapy.spiders import CSVFeedSpider
 
class VinosBlancosArania(CSVFeedSpider):
    name = "vinos"
 
    start_urls = [
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    ]

delimite = ';'
quotechar = '"'
headers = [
    'fixed density',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol',
    'quality'
]

def parse_row(self, response, row):
        print(type(row))
        with open('vinos.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(row['fixed density'] + '\n')