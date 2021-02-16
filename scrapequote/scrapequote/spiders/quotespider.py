import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = 'quotespider'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response):
        quote_container = response.xpath('//div[@class="quoteText"]')

        for quote in quote_container:
            quotes = quote.xpath('.//text()').get()
            author_name = quote.xpath('.//span[@class="authorOrTitle"]/text()').get()

            yield{
                'quote': quotes.strip(),
                'Name_of_Author': author_name.strip()
            }

        next_page = response.xpath('//a[@class="next_page"]/@href').get()

        if next_page is not None:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)