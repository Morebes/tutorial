import scrapy
from scrapy.loader import ItemLoader

from tutorial.items import Product
from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.utils.response import open_in_browser
    
class CssSpider(scrapy.Spider):
    name = 'css'
    allowed_domains = ['css.py']
    start_urls = ['https://bry.vkusvill.ru/goods/aktivator-kaltsiya-kapsuly-0-46-g-60-sht-63338.html']

    
    
    def parse(self, response):
        open_in_browser(response)
        card = ItemLoader(item=Product(), response=response)
        card.add_css('name','h1.Product__title::text')
        card.add_css('weight','div.ProductCard__weight::text')
        card.add_css('best_before','div.Product__bestbefore>div::text')
        card.add_css('price','div.Price__value')
        
    
        
        return card.load_item()
    

