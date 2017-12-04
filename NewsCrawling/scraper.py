import scrapy
from scrapy.http import Request

#globvar = 0
class NewsItem:
    def __init__(self):
        self.date = '1'
        self.url = 'a'

class BrickSetSpider(scrapy.Spider):
    name = "apple_news_spider"
    #start_urls = ['https://www.reuters.com/finance/stocks/company-news/AAPL.OQ?date=11302017']
    

    def start_requests(self):
        global globvar
        for year in range(2012, 2018):
            y = year
            for month in range(1, 13):
                if month < 10 :
                    m = '0' + str(month)
                else :
                    m = month
                for days in range(1, 32):
                    if days < 10: 
                        d = '0' + str(days)
                    else :
                        d = days
        
                    yield self.make_requests_from_url('https://www.reuters.com/finance/stocks/company-news/AAPL.OQ?date=%s%s%s'% (m, d, y))

    def parse(self, response):
        NEWS_SELECTOR = '.feature' #grab all news
        items= []
        for news in response.css(NEWS_SELECTOR):
            HEAD_SELECTOR = 'h2 a ::text'
            CONTENT_URL_SELECTOR = 'h2 a ::attr(href)'
            cururl = response.url[-8:]
            
            yield {
                'date' : cururl,
                'url' : news.css(CONTENT_URL_SELECTOR).extract_first(),
            }