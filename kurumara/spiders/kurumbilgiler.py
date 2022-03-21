# -*- coding: utf-8 -*-
import scrapy
import csv
from pathlib import Path


class KurumbilgilerSpider(scrapy.Spider):
    name = 'kurumbilgiler'
    allowed_domains = ['meb.k12.tr']
    path_to_file = './kurumbilgileri.csv'
    path = Path(path_to_file)
    if path.is_file():
        with open(path,'r', encoding='utf-8') as file:
            file = csv.DictReader(file)
            kurumlarwebsite=[]
            start_urls = []
            for col in file:
                '''b = xlrd.open_workbook('./kurumara/kurumbilgileri.csv')
                b.sheet_names()
                sh = b.sheet_by_name(u'Sayfa1')
                first_column = sh.col_values(6)
                start_urls = first_column '''
                start_urls.append(col['hakkinda'])
            #start_urls = kurumlarwebsite 

            def parse(self, response):
                okuladi=response.css("#dosya_liste h3::text").extract()
                resim=response.css("#dosya_liste .img-responsive::attr(src)").extract()
                telefon=response.css("#hakkinda_kutu .row:first-child div:nth-child(3)::text").extract()
                webadresi=response.css("#hakkinda_kutu .row:nth-child(4) div:nth-child(3)::text").extract()
                adres=response.css("#hakkinda_kutu .row:nth-child(5) div:nth-child(3)::text").extract()

                for item in zip(okuladi,resim,telefon,webadresi,adres):
                    kurumyenibilgileri={
                    
                        "kurum_adi":item[0],
                        "kurum_resim":item[1],
                        "kurum_tel":item[2],
                        "kurum_site":item[3],
                        "kurum_adres":item[4],
                    
                    }
                    print(kurumyenibilgileri)
                    yield kurumyenibilgileri
    else:
        print(f'The file {path_to_file} does not exist')

        
  