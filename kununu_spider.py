import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["kununu.com"]
    start_urls = ['https://www.kununu.com/de/ec4u-expert-consulting/kommentare']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for elem in response.css('article.company-profile-review'):
                    date = {
                               'date': elem.css('span::text')[1].extract(),
                               'title': elem.css('a::text')[0].extract(),
                               'rating': elem.css('div.tile-heading::text')[0].extract()
                            }
                    yield date
        next_page_url = response.css('a.btn.btn-default.btn-block::attr(href)')[0].extract()
        if next_page_url:
           print(" Aktuelle Seite" + next_page_url)
           next_page_url = response.urljoin(next_page_url)
           yield scrapy.Request(url=next_page_url, callback = self.parse)
