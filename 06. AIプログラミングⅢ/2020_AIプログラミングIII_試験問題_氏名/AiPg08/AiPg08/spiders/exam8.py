import scrapy
from scrapy.selector import Selector


class Exam8Spider(scrapy.Spider):
    name = 'exam8'
    start_urls = ['file://C:/temp/kujira.html']

    def parse(self, response):
        
        print("\nNomukun START\n")
        
        # print(response.css('li > a').getall())
        
        li_list = response.xpath('//li/a').getall()

        # print(li_list[0])
        
        for a in li_list:
            yield {
                'href' : Selector(text=a).xpath('//a/@href').get(),
                'text' : Selector(text=a).xpath('//a/text()').get()
            }

        print("\nNomukun END\n")