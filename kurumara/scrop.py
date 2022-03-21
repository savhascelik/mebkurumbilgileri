import scrapy

class Kurumara(scrapy.Spider):
    name = 'kurumara'
    start_urls = ['http://www.meb.gov.tr/baglantilar/okullar/?ILKODU=1']
    for x in range(1,82):
        text="http://www.meb.gov.tr/baglantilar/okullar/?ILKODU="+str(x)
        start_urls.append(text)

    def parse(self, response):
        okuladi = response.css(".table tr td:first-child a::text").extract()
        okulsite = response.css(".table tr td:first-child a::attr(href)").extract()
        okulhakkinda=response.css(".table tr td:nth-child(2) a::attr(href)").extract()
        for item in zip(okuladi,okulsite,okulhakkinda):
            okulbilgileri={
                "adi":item[0],
                "site":item[1],
                "hakkinda":item[2]
            }

            yield okulbilgileri