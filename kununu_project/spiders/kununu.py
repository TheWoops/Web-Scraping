import scrapy
import logging


class KununuSpider(scrapy.Spider):
    name = "kununu"
    allowed_domains = ["kununu.com"]

    # Reduce Log-Level of some Loggers to avoid "spam" messages in Command line
    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('scrapy.core.scraper')
        logger.setLevel(logging.INFO)
        logger2 = logging.getLogger('scrapy.core.engine')
        logger2.setLevel(logging.INFO)
        logger3 = logging.getLogger('scrapy.middleware')
        logger3.setLevel(logging.WARNING)
        logger4 = logging.getLogger('kununu')
        logger4.setLevel(logging.WARNING)
        super().__init__(*args, **kwargs)

    def start_requests(self):
        yield scrapy.Request('https://www.kununu.com/de/ec4u-expert-consulting/kommentare', self.parse)
        yield scrapy.Request('https://www.kununu.com/de/movilitas-consulting/kommentare', self.parse)

    def parse(self, response):
        print("Aktuelle Seite : {}".format(response.url))
        review_list = response.css('article.company-profile-review')
        for elem in review_list:
                    item = {
                               'url': response.url,
                               'date': elem.css('span::text')[1].extract(),
                               'title': elem.css('a::text')[0].extract(),
                               'rating': elem.css('div.tile-heading::text')[0].extract()
                            }
                    yield item

        next_page_url = response.css('a.btn.btn-default.btn-block::attr(href)') # does this attribute exist at all or is returned an empty list?
        if next_page_url:
           next_page_url = next_page_url[0].extract()
           next_page_url = response.urljoin(next_page_url)
           yield scrapy.Request(url=next_page_url, callback = self.parse)
        else:
            self.log('');self.log('');self.log('');self.log('');
            self.log('Last page reached: ' + response.url)
            self.log('Last page contained {} item(s)'.format(len(review_list)))
            self.log('');self.log('');self.log('');self.log('');self.log('');
