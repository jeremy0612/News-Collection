import scrapy
from scrapy_splash import SplashRequest
class ArticleSpider(scrapy.Spider):
    name = "Article"
    allowed_domains = ["www.foxnews.com"]
    start_urls = ["https://www.nytimes.com/2023/04/26/us/politics/trump-pence-testimony-jan-6.html"]
    handle_httpstatus_list = [404]

    def parse_(self, response):
        articles = response.xpath("//div[@class='content article-list']/article")
        for article in articles:
            yield scrapy.Request(
                url='http://www.foxnews.com/' + article.xpath("./div[@class='info']/header[@class='info-header']/h4/a/@href").get(),
                callback=self.detach
            )

    def parse(self, response):
        body = response.xpath("//div[@class='css-53u6y8']")
        #for article in body:
        result = {
            'Paragraph': body.xpath(".//p[@class='css-at9mc1 evys1bk0']/text()").get(),
        }
        yield result
        print(type(response.body))
        '''
        #result['Author'] = body.xpath(".//article/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline opinion']/span/a/text()").get()
        if len(body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/a/text()")) >= 1:
            result['Author'] = body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/a/text()").get()
        else:
            result['Author'] = body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/span/a/text()").get()
        result['Published'] = body.xpath(".//div[@class='article-date']/time/text()").get()
        result['Topic'] = body.xpath(".//div[@class='eyebrow']/a/text()").get()
        
        #print(result)
        yield result
        '''
'''
class ArticleSpider(scrapy.Spider):
    name = "Article"
    allowed_domains = ["www.foxnews.com"]
    start_urls = ["http://www.foxnews.com/politics","http://www.foxnews.com/world"]
    handle_httpstatus_list = [404]
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
    def parse(self, response):
        articles = response.xpath("//div[@class='content article-list']/article")
        for article in articles:
            yield scrapy.Request(
                url='http://www.foxnews.com/' + article.xpath("./div[@class='info']/header[@class='info-header']/h4/a/@href").get(),
                callback=self.detach
            )

    def detach(self, response):
        body = response.xpath("//main[@class='main-content']")
        result = {
            'Title': body.xpath(".//article/header/h1[@class='headline']/text()").get(),
        }
        #result['Author'] = body.xpath(".//article/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline opinion']/span/a/text()").get()
        if len(body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/a/text()")) >= 1:
            result['Author'] = body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/a/text()").get()
        else:
            result['Author'] = body.xpath(".//article[1]/header/div[@class='article-meta article-meta-lower']/div[@class='author-byline']/span/span/a/text()").get()
        result['Published'] = body.xpath(".//div[@class='article-date']/time/text()").get()
        result['Topic'] = body.xpath(".//div[@class='eyebrow']/a/text()").get()

        #print(result)
        yield result


class CategorySpider(scrapy.Spider):
    name = "Category"
    allowed_domains = ["www.foxnews.com"]
    start_urls = ["http://www.foxnews.com"]

    def parse(self, response):
        categories = ['politics', 'world'] #['politics', 'world', 'opinion']
        for category in categories:
            category_url = f"{self.start_urls[0]}/{category}"
            yield scrapy.Request(url=category_url, callback=ArticleSpider().parse)
    def parse_category(self, response):
        spider = ArticleSpider()
        yield from spider.parse(response)
'''