# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

def dbHandle():
    conn=pymysql.connect(
        host="39.108.173.192",
        user="OutisJie",
        password="123456",
        charset="utf8",
        use_unicode=False,
        db='android',
        port=3306
    )
    return conn

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        dbObject=dbHandle()
        cursor=dbObject.cursor()
        sql="INSERT INTO article(article_title,article_subtitle,article_author,article_date,article_theme,article_bodyhtml,article_img,article_imgs,article_text) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (item['article_title'],
                                 item['article_subtitle'],
                                 item['article_author'],
                                 item['article_date'],
                                 item['article_theme'],
                                 item['article_bodyhtml'],
                                 item['article_img'],
                                 item['article_imgs'],
                                 item['article_text']
                                 ))
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()
        return item
