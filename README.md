# mebokulbilgileri

MEB'e bağlı kurumların  http://www.meb.gov.tr/baglantilar/okullar/ adresinden okunmasını sağlayan BOT.

#kullanımı
Öncelikle aşağıdaki kod bloğu ile kurumara botu ile botun dizininde kurumbilgileri.csv dosyası oluşturacak ve adresten "okuladi,okulsite,okulhakkinda,okulharita" bilgilerini çekecektir.

`scrapy crawl kurumara`

Daha sonra okullara ait okuladi,resim,telefon,webadresi,adres bilgilerini çekmek için aşağıdaki kod bloğu girilerek kurumbilgiler botu çalıştırılabilir. Bu botun çalışması için kurumara botunun çalışması ve kurumbilgileri.csv dosyasının oluşmuş olması gerekmekte çünkü bot bu dosyadan okulhakkinda url adresinden kazıma yapmakta.

`scrapy crawl kurumbilgiler -o kurumdetaybilgiler.csv`
