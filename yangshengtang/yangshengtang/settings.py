# -*- coding: utf-8 -*-

# Scrapy settings for yangshengtang project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yangshengtang'

SPIDER_MODULES = ['yangshengtang.spiders']
NEWSPIDER_MODULE = 'yangshengtang.spiders'
ITEM_PIPELINES = ['yangshengtang.pipelines.YangShTPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yangshengtang (+http://www.yourdomain.com)'



FILE_STORE = ''
FILE_EXPIRES = 180
MEDIA_FILE_EXPIRES = 180
###FILE_EXTENTION = ['.flv','hd2','.mp4', '.swf']

URL_GBK_DOMAIN = []
ATTACHMENT_FILENAME_UTF8_DOMAIN = []

#for download middleware
DOWNLOAD_TIMEOUT = 600

USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
