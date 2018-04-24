# -*- coding: utf-8 -*-

# Scrapy settings for scrapydemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#日志等级：
# CRITICAL
# ERROR
# WARNING
# DEBUG
# INFO
# LOG_LEVEL = 'DEBUG'
# LOG_FILE = 'log.txt'


#日志的日期格式
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'




BOT_NAME = 'scrapydemo'

SPIDER_MODULES = ['scrapydemo.spiders']
NEWSPIDER_MODULE = 'scrapydemo.spiders'

CONCURRENT_ITEMS = 100  #Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值 默认: 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapydemo (+http://www.yourdomain.com)'

# Obey robots.txt rules
#是否遵循robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32   # Scrapy downloader 并发请求(concurrent requests)的最大值。

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数:
#DOWNLOAD_DELAY = 3



#下载器超时时间(单位: 秒)。
#DOWNLOAD_TIMEOUT = 180


# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16   #对单个网站进行并发请求的最大值。






# #对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定，
# 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
#该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。
#CONCURRENT_REQUESTS_PER_IP = 16




# Disable cookies (enabled by default)
#设置cookies是否关闭 有些网站通过cookie的使用发现爬虫行为
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False



# Override the default request headers:
#Scrapy HTTP Request使用的默认header。由 DefaultHeadersMiddleware 产生。
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapydemo.middlewares.ScrapydemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapydemo.middlewares.ScrapydemoDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html


ITEM_PIPELINES = {
   'scrapydemo.pipelines.ScrapydemoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings


# 这几行注释的作用是，Scrapy会缓存你有的Requests!当你再次请求时，
# 如果存在缓存文档则返回缓存文档，而不是去网站请求，这样既加快了本地调试速度，也减轻了 网站的压力。一举多得
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
