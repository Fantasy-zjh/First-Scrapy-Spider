# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_title = scrapy.Field()
    article_subtitle = scrapy.Field()
    article_bodyhtml=scrapy.Field()
    article_author=scrapy.Field()
    article_date=scrapy.Field()
    article_theme=scrapy.Field()
    article_img=scrapy.Field()
    article_imgs=scrapy.Field()
    article_text=scrapy.Field()