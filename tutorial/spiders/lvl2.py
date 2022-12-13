import scrapy

from tutorial.items import Product


class Lvl2Spider(scrapy.Spider):
    name = 'lvl2'
    allowed_domains = ['bry.vkusvill.ru']
    start_urls = ['https://bry.vkusvill.ru/offers/']

    def parse(self, response):
        product_list = []
        for card in response.css('div.ProductCards__item'):
            product = Product()
            product['name'] =card.css('a.ProductCard__link::text').get().strip()
            product['weight'] = card.css('div.ProductCard__weight::text').get().strip()
            product['price'] = card.css('span.Price>span.Price__value::text').get().strip() + 'Р.'
            product['old_price'] = card.css('span._last>span.Price__value::text').get().strip() + 'Р.'
            product['image'] = card.css('img.ProductCard__imageImg::attr(src)').get()
            product['link'] = 'https://bry.vkusvill.ru/'+ card.css('div.ProductCard__imageInner>a::attr(href)').get().strip()
            
            product_list.append(product)
            
        return product_list
