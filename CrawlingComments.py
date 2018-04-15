import scrapy


class MainSpider (scrapy.Spider):
    name = 'mainSpider'
    start_urls = ['https://www.booking.com/reviews/br/hotel/matiz-salvador.pt-br.html?aid=304142;label=gen173nr-1DCAEoggJCAlhYSDNYBGggiAEBmAEtwgEKd2luZG93cyAxMMgBDNgBA-gBAZICAXmoAgM;sid=941ae19fdb57991b30f93ef574319a9f']

    def parse(self, response):
        self.log('Eu estou em() :'.format(response.url))
        texts = response.xpath('//span[@itemprop="reviewBody"]/text()').extract()

        for text in texts:
            yield{
                'Text': text
            }

