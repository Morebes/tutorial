import scrapy 

from tutorial.items import Product


class QuotesSpider(scrapy.Spider):
    name = "xpath"
    start_urls =  ("https://bry.vkusvill.ru/goods/avokado-khass-artfruit-svezhee-700-g-65881.html",)

    def parse(self, response):
        product = Product()
        
        product['name'] = response.xpath('//h1/text()').get().strip()
        product['weight'] = response.xpath('//div[@class="ProductCard__weight nobr rtext _desktop-md _tablet-sm _mobile-sm"]/text()').get().strip()
        product['price'] = response.xpath('//span[@class="Price__value"]/text()').get().strip() + ' P.'
        product['description'] = ''.join(response.xpath('//div[@class="Product__descText rtext _desktop-md _tablet-md _mobile-md b400 js-product-text-cut"]/text()').getall())
        product['best_before'] = response.xpath('//div[@class="rtext _desktop-md _tablet-md _mobile-md b500"]/text()').get().strip()
        product['energy_exciter'] = response.xpath('//div[@class="Product__details-text rtext _desktop-md _tablet-md _mobile-md b500"]/text()').get().strip()

        
        return product

