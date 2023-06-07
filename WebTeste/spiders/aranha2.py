import json
import scrapy

with open('D:\Documentos\MeusProjetos\WebTeste\links.json') as file:
    dados = json.load(file)
    valor = dados[0]

    link_1 = valor['link1']
    link_2 = valor['link2']
    link_3 = valor['link3']
    link_4 = valor['link4']


class QuotesSpiderSecundário(scrapy.Spider):
    name = 'extracao'
    start_urls = [link_1, link_2, link_3, link_4]

    def parse(self, response):
        massa = response.xpath("//div[@property='rnews:articleBody']")

        for text in massa:
            yield{
                'titulo': text.xpath("//h1[@class='documentFirstHeading']//text()").get(),
                'autor' : text.xpath("//div[@property='rnews:articleBody']//p[1]//text()").get(),
                'primeiro_paragrafo' : text.xpath("//div[@property='rnews:articleBody']//p[2]//text()").get()
            }
        

    

