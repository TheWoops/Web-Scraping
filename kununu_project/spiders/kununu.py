import scrapy


class KununuSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["kununu.com"]
    start_urls = ['https://www.kununu.com/de/ec4u-expert-consulting/kommentare']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        review_list = response.css('article.company-profile-review')
        for elem in review_list:
                    date = {
                               'date': elem.css('span::text')[1].extract(),
                               'title': elem.css('a::text')[0].extract(),
                               'rating': elem.css('div.tile-heading::text')[0].extract()
                            }
                    yield date

        next_page_url = response.css('a.btn.btn-default.btn-block::attr(href)') # does this attribute exist at all or is returned an empty list?
        if next_page_url:
           next_page_url = next_page_url[0].extract()
           print(" Aktuelle Seite" + next_page_url)
           next_page_url = response.urljoin(next_page_url)
           yield scrapy.Request(url=next_page_url, callback = self.parse)
        else:
            self.log('');self.log('');self.log('');self.log('');
            self.log('Last page reached: ' + response.url)
            self.log('Last page contained {} item(s)'.format(len(review_list)))
            self.log('');self.log('');self.log('');self.log('');self.log('');
