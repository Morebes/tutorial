from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

from tutorial.processors import strip

class ProductLoader(ItemLoader):
    default_input_processor = TakeFirst()
    default_output_processor = MapCompose(strip)