# -*- coding: utf-8 -*-
import scrapy
import  re

import requests
from lxml import etree
from scrapy import Request
from scrapy.selector import  Selector
import uuid
import random
from scrapydemo.items import ScrapydemoItem #这是定义需要保存的字段（导入scrapydemo项目中。items文件中的ScrapydemoItem类）
from scrapydemo.items import FansTtem

class BiduspiderSpider(scrapy.Spider):
    # 这里是将爬虫定义为scrapy.Spider这个类下的一个实例。
    # Spider这个类定义了爬虫的很多基本功能，我们直接实例化就好，
    # 省却了很多重写方法的麻烦。

    host = "http://top.hengyan.com"
    name = 'scrapydemo' # 这的名字，这个非常重要。

    allowed_domains = ['top.hengyan.com']
    # start_urls = ['http://www.taojintimes.com/a/about/']
    #这是爬虫开始干活的地址，必须是一个可迭代对象。



    list=[
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]



    def start_requests(self):
        urls = [
            "http://top.hengyan.com/quanben/"
        ]
        for url in urls:
            yield  scrapy.Request(url=url,callback=self.parse_book)


    def parse_book(self, response):
        selector = Selector(response=response)

        # 爬虫收到上面的地址后，就会发送requests请求，在收到服务器返回的内容后，就将内容传递给parse函数。在这里我们重写函数，达到我们想要的功能。
        uls = selector.xpath("//ul[not(@class='title')]")
        for ul in uls:
             # try:
                bookname = ul.xpath("li[@class='bookname']/a[@class='bn' or @class='bn vip']/text()").extract()  # 书名
                author = ul.xpath("li[@class='author']/text()").extract()  # 作者
                novelurl = ul.xpath("li[@class='bookname']/a[@class='bn' or @class='bn vip']/@href").extract()  # 书籍地址
                if   len(bookname)  and  len(author) and len(novelurl):
                    tempuuid = uuid.uuid1()
                    demoItems = ScrapydemoItem()
                    demoItems["bookname"] = bookname[0]
                    demoItems["author"] = author[0]
                    demoItems["novelurl"] = novelurl[0]
                    demoItems["uuid"] = tempuuid


                    if len(novelurl):
                        r =  requests.get(novelurl[0])
                        if r.status_code  == 200:
                            numselector  = etree.HTML(r.content,parser=etree.HTMLParser(encoding='utf-8'))
                            tempnum = numselector.xpath("//div[@class='giftnum']/text()")
                            if tempnum[0]:
                                tempnum2 = re.split('(\d+)', tempnum[0])
                                demoItems['giftnum'] = tempnum2[1]

                            temfansurl = numselector.xpath("//a[@class='wen']/@href")
                            fansr = requests.get(temfansurl[0])
                            if fansr.status_code == 200:
                                fanslistselector = etree.HTML(fansr.content, parser=etree.HTMLParser(encoding='utf-8'))
                                fansurls = fanslistselector.xpath("//ul[@class='item']")
                                for fansurl in fansurls:
                                    fanslaa = fansurl.xpath("li/text()")
                                    fansnickname = fansurl.xpath("li/a/text()") #粉丝昵称
                                    if len(fansnickname) and len(fansrank) and len(fanslevel) and len(fansvalue):
                                        fansItem = FansTtem()
                                        fansItem['fansnickname'] = fansnickname
                                        fansItem['fansrank'] = fanslaa[0] #粉丝排名
                                        fansItem['fanslevel'] = fanslaa[1] #粉丝等级
                                        fansItem['fansvalue'] = fanslaa[2] #粉丝值
                                        fansItem['bookuuid'] = tempuuid
                                    yield fansItem

                    yield demoItems
             # except Exception:
             #     pass


        url_next = selector.xpath("//p[@class='pager']/a[text()='下一页']/@href").extract()
        if url_next:
            yield Request(url=self.host+url_next[0],callback=self.parse_book,dont_filter=True)












