# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from  scrapydemo.items import ScrapydemoItem
from  scrapydemo.items import FansTtem
class ScrapydemoPipeline(object):

    def __init__(self):
        self.count = 0;
        # 创建连接
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='world', charset='utf8')
        # 创建游标
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, ScrapydemoItem):
            sql = "insert into book(id,bookname,author,novelurl,giftnum) VALUES (%s,%s,%s,%s)"
            lis = (item['uuid'], item['bookname'], item['author'], item['novelurl'], item['giftnum'])
            self.cur.execute(sql, lis)
            self.conn.commit()
            self.count = self.count+1

        elif isinstance(item, FansTtem):
            sql = "insert into book(bookid,bookname,author,novelurl,giftnum) VALUES (%s,%s,%s,%s)"
            lis = (item['bookuuid'], item['bookname'], item['author'], item['novelurl'], item['giftnum'])
            self.cur.execute(sql, lis)
            self.conn.commit()
            self.count = self.count + 1

        if self.count == 1000:
            print("try reconnecting")
            self.count = 1
            self.cur.close()
            self.conn.close()
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='world',
                                        charset='utf8')
            self.cur = self.conn.cursor()
            print("reconnect")
        return item




