import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.loader import ProductLoader
from tutorial.items import Product
    
class SpiderSpider(scrapy.Spider):
    name = 'lvl3'
    start_urls = ['https://vkusvill.ru/goods/gotovaya-eda/']
    
    def parse(self,response):
        for link in response.css('div.ProductCard__content>a.ProductCard__link::attr(href)').getall():
            yield scrapy.Request(url='https://vkusvill.ru'+link,callback=self.get_item)
            
        next_page = response.xpath('//span[contains(. , "Вперёд")]/../@href').get()

        if next_page is not None:
           next_page_url = 'https://vkusvill.ru' + next_page
           yield response.follow(next_page_url, callback=self.parse) 

        
    def get_item(self,response):
        loader = ProductLoader(item=Product(),response=response)
        
        loader.add_css('name','h1::text')
        loader.add_css('weight','div.ProductCard__weight::text')
        loader.add_css('price','span.Price__value::text')
        loader.add_css('best_before','div.Product__bestbefore>div::text')
        loader.add_css('image','div.ProductGallery__image>img.lazyload::attr(src)')
        loader.add_css('energy_exciter','div.Product__details-text::text')
        loader.add_value('link',response.url)

        return loader.load_item()