# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    uuid = scrapy.Field()
    #书名
    bookname = scrapy.Field()

    #作者
    author = scrapy.Field()

    #地址
    novelurl = scrapy.Field()

    #总共打赏
    giftnum = scrapy.Field()




class FansTtem(scrapy.Item):
    bookuuid = scrapy.Field()
    bookid = scrapy.Field()
    fansnickname = scrapy.Field()
    fansrank = scrapy.Field()
    fanslevel = scrapy.Field()
    fansvalue = scrapy.Field()


