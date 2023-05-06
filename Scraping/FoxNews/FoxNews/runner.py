import scrapy 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.Article import ArticleSpider#, CategorySpider

if __name__ == "__main__":
    process = CrawlerProcess({
        'FEED_URI': 'data.json',
        'FEED_FORMAT': 'json'
    })
    process.crawl(ArticleSpider)
    process.start()