import scrapy
from ..items import ScrapyspiderItem
class ScrapySpider(scrapy.Spider):
    name='quotes'
    start_urls=['https://quotes.toscrape.com/']

    def parse(self,response):
        all_quotes=response.css("div.row::text").extract()
        for qoutes in all_quotes:
         title=response.css('title::text').extract()
         author=response.css('.author::text').extract()
         tags=response.css('.tag::text').extract()
         items=ScrapyspiderItem()
         items['title']=title
         items["author"]=author
         items["tags"]=tags
         yield items
        
