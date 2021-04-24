import scrapy
from scraper.items import DatosScrapyItem
from scrapy.http import Request
from .urls_scraper import urls_espana
import re

class TextoSpider(scrapy.Spider):
    name = 'texto'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/']

    def parse(self, response):
        urls = response.xpath('//h2/a/@href').extract()
        for url in urls:
            absolute_urls = response.urljoin(url)
            yield Request(absolute_urls, callback=self.parse_corte_ingles)
        
        for url_espana in urls_espana:
            yield Request(url_espana)
        
    def parse_corte_ingles(self, response):
        item = DatosScrapyItem()
        #precio_original = None


        title_sucio = response.xpath('//h1/text()').extract()
        title_sucio = str(title_sucio)
        title = title_sucio.strip("[']")

        denominacion_de_origen_sucio = response.xpath("//dd[contains(text(), 'DO')]/text()").extract()
        denominacion_de_origen_sucio = str(denominacion_de_origen_sucio)
        denominacion_de_origen = denominacion_de_origen_sucio.strip("[']")
        
        informacion_adicional_sucio = response.xpath('//div[@class="product_detail-description-in-image c8  font-xs"]/p/text()').extract()
        informacion_adicional_sucio = str(informacion_adicional_sucio)
        informacion_adicional = informacion_adicional_sucio.strip("[']")

        try:
            precio_final = response.xpath('//meta[@itemprop="price"]/@content').extract_first()
            
        except Exception:
            print("Oops!  That was no valid number.  Try again...")
            
        marca = response.xpath('//meta[@itemprop="name"]/@content').extract()[3]
        

        item['title'] = title
        item['precio_rebajado'] = response.xpath('//p[@class="price _big _sale"]').extract()
        item['precio_original'] = precio_final
        item['denominacion_de_origen'] = denominacion_de_origen
        item['imagen'] = response.xpath('//img/@src').extract()[1]
        item['informacion_adicional'] = informacion_adicional
        item['marca'] = marca



        yield item
    pass