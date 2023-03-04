import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.xpath("//ol[@class='row']/li")
        for book in books:
            yield {
                'image': response.urljoin(book.xpath(".//div[@class = "
                                     "'image_container']/a/img/@src").get()),

                'price': book.xpath(".//p[@class='price_color']/text()").get(),
                'title': book.xpath(".//h3/a/@title").get()
            }
