import scrapy

class NecklaceSet(scrapy.Spider):
    name = 'necklace'
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    # Defining a parse function to create a dictionary of products.
    def parse(self, response):
        # Going through <li> under <ul id="JsonProductList">
        for product in response.xpath('//ul[@id="JsonProductList"]/li'):
            yield {
                'id': product.css("::attr(data-pos)").get(),
                'name': product.css("::attr(data-name)").get(),
                'price': product.css("::attr(data-price)").get(),
                'color': product.css("::attr(data-color)").get(),
                'url': product.css("::attr(data-url)").get(),
            }