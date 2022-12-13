import scrapy
from itemloaders.processors import MapCompose, TakeFirst

from tutorial.processors import strip

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    best_before = scrapy.Field()
    energy_exciter = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()

    
    
