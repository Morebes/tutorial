from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.loader import ProductLoader
from tutorial.items import Product
    
class SpiderSpider(CrawlSpider):
    name = 'lvl3'
    start_urls = ['https://bry.vkusvill.ru/goods/gotovaya-eda/']
    
    rules = [Rule(LinkExtractor(allow=r'/goods/.*.html'), callback='parse', follow=True),
            Rule(LinkExtractor(allow=r'/goods/'), follow=True),
             ]

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
