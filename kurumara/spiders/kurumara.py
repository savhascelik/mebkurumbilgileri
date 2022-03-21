# -*- coding: utf-8 -*-
from itertools import count
from posixpath import split
import scrapy
import urllib.parse
iterator = count(start = 0, step = 1)
kurumbilgileri=[]
kurumad=[]
ilplaka=[]
ilad=[]
ilceno=[]
ilcead=[]
kurumkodu=[]
class KurumaraSpider(scrapy.Spider):
    name = 'kurumara'
    allowed_domains = ['http://www.meb.gov.tr/baglantilar/okullar/?ILKODU=1']
    start_urls = ['http://www.meb.gov.tr/baglantilar/okullar/?ILKODU=1']

    
    for x in range(1,82):
        text="http://www.meb.gov.tr/baglantilar/okullar/?ILKODU="+str(x)
        start_urls.append(text)
        
    
    def parse(self, response):
        kurumuzunad = response.css(".table tr td:first-child a::text").extract()
        kurumsite = response.css(".table tr td:first-child a::attr(href)").extract()
        kurumhakkinda=response.css(".table tr td:nth-child(2) a::attr(href)").extract()
        kurumharita=response.css(".table tr td:nth-child(3) a::attr(data-src)").extract()
        detay=kurumuzunad[next(iterator)].split("-")
        ilad.append(detay[0])
        ilcead.append(detay[1])
        kurumad.append(detay[2])
        hakkinda=kurumhakkinda[next(iterator)].split("/")
        ilplaka.append(hakkinda[4])
        ilceno.append(hakkinda[5])
        kurumkodu.append(hakkinda[6])
        for item in zip(ilplaka,ilad,ilceno,ilcead,kurumkodu,kurumad, kurumuzunad,kurumsite,kurumhakkinda,kurumharita):
            print("item {} ",item)
            kurumbilgileri={
                "ilplaka":item[0],
                "ilad":item[1],
                "ilceno":item[2],
                "ilcead":item[3],
                "kurumkodu":item[4],
                "kurumad":item[5],
                "kurumuzunad":item[6],
                "site":item[7],
                "hakkinda":item[8],
               "kurumharita":item[9],
            }
            

            yield kurumbilgileri
  