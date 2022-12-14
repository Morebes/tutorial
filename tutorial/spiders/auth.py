import scrapy
from scrapy.utils.response import open_in_browser

from tutorial.items import Card
class JuniorSpider(scrapy.Spider):
    name = "junior"
    count_list = 7
    start_urls = ['https://github.com/login']
        
        

    def parse(self,response):
        token = response.css('input[name="authenticity_token"]').get()
        return scrapy.FormRequest.from_response(response=response,formdata={
            'login':'morebesor@gmail.com',
            'password':'lolinekotrap1',
        },callback=self.out)
        
    def out(self,response):
        open_in_browser(response)
        return print(response.css('body').get())
    
   
            
            
        
        