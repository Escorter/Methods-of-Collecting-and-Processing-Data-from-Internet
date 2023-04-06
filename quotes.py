# Паук 'quotes' логинится на сайт quotes.toscrape.com,
# а после авторизации парсит цитаты с открывшейся страницы

import scrapy
from scrapy import FormRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/login"]

    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrf_token']/@value").get()
        print(65 * '*')
        print(f'{csrf_token=}')
        print(65 * '*')

        yield FormRequest.from_response(response, formxpath='//form',
                                        formdata={'csrf_token': csrf_token,
                                                  'username': 'admin',
                                                  'password': 'admin'},
                                        callback=self.after_login)

    def after_login(self, response): # метод, что делать после авторизации
        quotes = response.xpath("//div[@class = 'quote']")
        print(65 * '&')
        print('-=СОДЕРЖИМОЕ СТРАНИЦЫ=-')
        for item in quotes:
            q = item.css('span.text::text').get()
            print(q)
        print(65 * '&')