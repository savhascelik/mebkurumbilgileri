# -*- coding: utf-8 -*-
import scrapy
import xlrd

class ResimtelSpider(scrapy.Spider):
    name = 'resimtel'
    allowed_domains = ['meb.k12.tr']

    b = xlrd.open_workbook('C:\scrapy\okulara\kurumbilgilerson.xlsx')
    b.sheet_names()
    sh = b.sheet_by_name(u'Sayfa1')
    first_column = sh.col_values(6)
    start_urls = first_column

    def parse(self, response):
        
        okuladi=response.css("#dosya_liste h3::text").extract()
        resim=response.css("#dosya_liste .img-responsive::attr(src)").extract()
        telefon=response.css("#hakkinda_kutu .row:first-child div:nth-child(3)::text").extract()
        webadresi=response.css("#hakkinda_kutu .row:nth-child(4) div:nth-child(3)::text").extract()
        adres=response.css("#hakkinda_kutu .row:nth-child(5) div:nth-child(3)::text").extract()
      
        for item in zip(okuladi,resim,telefon,webadresi,adres):
            kurumbilgileri2={
            
               "kurum_adi":item[0],
               "kurum_resim":item[1],
               "kurum_tel":item[2],
               "kurum_site":item[3],
               "kurum_adres":item[4],
           
            }
            
            

            yield kurumbilgileri2
  