import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://www.zoevers.nl/elektrische-fietsen/']
