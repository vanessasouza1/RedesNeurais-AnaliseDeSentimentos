import scrapy
from scrapy.selector import Selector

####################Links positivos ############
##link 1 : https://www.booking.com/reviews/br/hotel/windsor-miramar.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 2: https://www.booking.com/reviews/br/hotel/copacabana-palace.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 3: https://www.booking.com/reviews/br/hotel/copacabana-palace.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page=2;r_lang=pt;rows=75&
# link 4: https://www.booking.com/reviews/br/hotel/villa-dos-corais.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 5: https://www.booking.com/reviews/br/hotel/vila-dos-orixas-boutique.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page=2;r_lang=pt;rows=75&
# link 6: https://www.booking.com/reviews/br/hotel/olympia-residence.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 7: https://www.booking.com/reviews/br/hotel/nb-hoteis.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f



###################Links Negativos###################
# link 1: https://www.booking.com/reviews/br/hotel/aero-plaza.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 2: https://www.booking.com/reviews/br/hotel/fit-sao-paulo.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 3: https://www.booking.com/reviews/br/hotel/hostel-villa-santana.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 4: https://www.booking.com/reviews/br/hotel/mundo-novo.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 5: https://www.booking.com/reviews/br/hotel/luar-de-itapua.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 6: https://www.booking.com/reviews/br/hotel/arthemis-e-pousada.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 7: https://www.booking.com/reviews/br/hotel/portal-torres.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f
# link 8: https://www.booking.com/reviews/br/hotel/piacenza.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f


class MainSpider (scrapy.Spider):
    name = 'mainSpider'
    start_urls = ['https://www.booking.com/reviews/br/hotel/piacenza.pt-br.html?aid=381641;sid=941ae19fdb57991b30f93ef574319a9f']

    def parse(self, response):
        self.log('Eu estou em() :'.format(response.url))

        #texts =response.xpath('//p[contains(@class, "review_neg")]').extract() ### funcionou só q ta pegando as tags

        texts = response.xpath('//p[contains(@class, "review_neg")]/span/text()').extract()  ### funcionou só q ta pegando as tags


        for text in texts:
            yield{
                'Text': text
            }
