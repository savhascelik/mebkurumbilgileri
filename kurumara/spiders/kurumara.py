# -*- coding: utf-8 -*-
import scrapy
import urllib.parse


class KurumaraSpider(scrapy.Spider):
    name = 'kurumara'
    allowed_domains = ['http://www.meb.gov.tr/baglantilar/okullar/?ILKODU=1']
    start_urls = ['http://www.meb.gov.tr/baglantilar/okullar/?ILKODU=1']
    kurumbilgileri=[]
    for x in range(2,82):
        text="http://www.meb.gov.tr/baglantilar/okullar/?ILKODU="+str(x)
        start_urls.append(text)
        

    def parse(self, response):
        okuladi = response.css(".table tr td:first-child a::text").extract()
        okulsite = response.css(".table tr td:first-child a::attr(href)").extract()
        okulhakkinda=response.css(".table tr td:nth-child(2) a::attr(href)").extract()
        okulharita=response.css(".table tr td:nth-child(3) a::attr(data-src)").extract()
     
        for item in zip(okuladi,okulsite,okulhakkinda,okulharita):
            kurumbilgileri={
                "adi":item[0],
                "site":item[1],
                "hakkinda":item[2],
               "okulharita":item[3],
            }
            

            yield kurumbilgileri
  