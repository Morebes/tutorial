import scrapy

from tutorial.loader import ProductLoader
from tutorial.items import Product

class Lvl3Spider(scrapy.Spider):
    name = 'lvl3'
    allowed_domains = ['bry.vkusvill.ru']
    
    def start_requests(self):
        urls = ['https://bry.vkusvill.ru/goods/gotovaya-eda/',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_link)

    def parse_link(self, response):
        for link in response.css('div.ProductCard__content>a.ProductCard__link::attr(href)').getall():
            yield scrapy.Request(url=response.urljoin(link),callback=self.parse)
            
    def parse(self,response):
        loader = ProductLoader(item=Product(),response=response)
        
        loader.add_css('name','h1::text')
        loader.add_css('weight','div.ProductCard__weight::text')
        loader.add_css('price','span.Price__value::text')
        loader.add_css('best_before','div.Product__bestbefore>div::text')
        loader.add_css('image','div.ProductGallery__image>img.lazyload::attr(src)')
        loader.add_css('energy_exciter','div.Product__details-text::text')
        loader.add_value('link',response.url)

        return loader.load_item()
