# -*- coding: utf-8 -*-
from itertools import count
import scrapy
import csv
from pathlib import Path
iterator = count(start = 0, step = 1)
kurumyenibilgileri=[]
kurumad=[]
ilplaka=[]
ilad=[]
ilceno=[]
ilcead=[]
kurumkodu=[]
class KurumbilgilerSpider(scrapy.Spider):
    name = 'kurumbilgiler'
    allowed_domains = ['meb.k12.tr']
    path_to_file = './kurumbilgileri.csv'
    path = Path(path_to_file)
    if path.is_file():
        with open(path,'r', encoding='utf-8') as file:
            file = csv.DictReader(file)
            start_urls = []

            for col in file:
                start_urls.append(col['hakkinda'])
                
            def parse(self, response):
                kurumadi=response.css("#dosya_liste h3::text").extract()
                resim=response.css("#dosya_liste .img-responsive::attr(src)").extract()
                telefon=response.css("#hakkinda_kutu .row:first-child div:nth-child(3)::text").extract()
                webadresi=response.css("#hakkinda_kutu .row:nth-child(4) div:nth-child(3)::text").extract()
                adres=response.css("#hakkinda_kutu .row:nth-child(5) div:nth-child(3)::text").extract()
                hakkinda=self.start_urls[next(iterator)].split("/")
                ilplaka.append(hakkinda[4])
                ilceno.append(hakkinda[5])
                kurumkodu.append(hakkinda[6])

                for item in zip(ilplaka,ilceno,kurumkodu,kurumadi,resim,telefon,webadresi,adres):
                    kurumyenibilgileri={
                        "ilplaka":item[0],
                        "ilceno":item[1],
                        "kurumkodu":item[2],
                        "kurum_adi":item[3],
                        "kurum_resim":item[4],
                        "kurum_tel":item[5],
                        "kurum_site":item[6],
                        "kurum_adres":item[7],
                    
                    }
                    yield kurumyenibilgileri
    else:
        print(f'The file {path_to_file} does not exist')

        
  