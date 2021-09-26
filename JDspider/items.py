# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JDCommentItem(scrapy.Item):
    nickname = scrapy.Field()
    score = scrapy.Field()
    productColor = scrapy.Field()
    content = scrapy.Field()
    referenceName = scrapy.Field()
    referenceTime = scrapy.Field()
