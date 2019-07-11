import scrapy
from bs4 import BeautifulSoup

class AloNhaDatSpide(scrapy.Spider):
    name = "alonhadat"

    def start_requests(self):
        urls = ['']
        for url in urls:
            yield scrapy.Request(url=url, 
            callback=self.parse)

    def parse(self, response):
        response.css()