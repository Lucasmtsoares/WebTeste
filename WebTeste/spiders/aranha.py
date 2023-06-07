import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'lista'
    start_urls = ['https://www2.ifal.edu.br/']

    def parse(self, response):
        corpo = response.xpath("//ul[@id='tile_banner_rotativo']")

        for q in corpo:
            

            yield {
                'link1': q.xpath("//li[@id='banner2']//a/@href").get(),
                'link2': q.xpath("//li[@id='banner2']//a/@href").get(),
                'link3': q.xpath("//li[@id='banner3']//a/@href").get(),
                'link4': q.xpath("//li[@id='banner4']//a/@href").get()
            }
