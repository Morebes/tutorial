import scrapy
from itemloaders.processors import MapCompose, TakeFirst

from tutorial.processors import strip,TakeSecond

class Product(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(strip),
                        output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(strip),
                         output_processor=TakeFirst())
    weight = scrapy.Field(input_processor=MapCompose(strip),
                          output_processor=TakeFirst())
    best_before = scrapy.Field(input_processor=MapCompose(strip),
                               output_processor=TakeFirst())
    energy_exciter = scrapy.Field(input_processor=MapCompose(strip),
                                  output_processor=TakeFirst())
    image = scrapy.Field()
    link = scrapy.Field(output_processor=TakeFirst())

    
    
