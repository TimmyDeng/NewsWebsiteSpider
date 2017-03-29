import ConfigParser
import codecs
import os
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import FormRequest, Request
from Common import ConfigSectionMap
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
import db_setting

class NewsSpider(CrawlSpider):
    name = "newsSpider"
    base_url = ""
    host = ""
    referer = ""
    user_agent = ""
    article_no = 0


    def initParameters(self):
        Config = ConfigParser.ConfigParser()
        Config.read(os.path.dirname(__file__) + "/config.ini")
        self.base_url = ConfigSectionMap("input", Config )['base_url']
        self.host = ConfigSectionMap("input", Config )['host']
        self.referer = ConfigSectionMap("input", Config )['referer']
        self.user_agent = ConfigSectionMap("input", Config )['user_agent']
        self.client = MongoClient(db_setting.db_host, db_setting.db_port)
        self.db = self.client[db_setting.db_store]
        self.table = self.db[db_setting.db_table]

    def start_requests(self):
        self.initParameters()
        yield Request(self.base_url,headers={'Host': self.host,
            'Referer': self.referer,
            'Upgrade-Insecure-Requests':'1','User-Agent': self.user_agent}
            , callback=self.parse_page)


    def parse_page(self, response):
        fileName = "articles_url_list.csv"
        print "start to parse html ........................................."
        article_url_list = []

        with codecs.open(fileName, "w","utf-8") as myfile:
            for each in response.css("div.fc-item__content"):
                tag_a = each.xpath(".//a")
                if  tag_a is not None:
                    article_url = tag_a.xpath('@href').extract_first()
                    item_title = tag_a.xpath('.//text()').extract_first()
                    article_url_list.append(article_url)
                    myfile.write(item_title + "\t" + article_url + "\n" )
        for url in article_url_list:
            self.article_no += 1
            yield Request(url,headers={'Host': self.host,
                'Referer': self.referer,
                'Upgrade-Insecure-Requests':'1','User-Agent': self.user_agent}
                , callback=self.article_parse_page, meta={'article_no': self.article_no})


    def article_parse_page(self, response):
        article_url = response.url
        article_author = ""
        headline = ""
        article_text = ""
        author_url = ""

        author_span = response.css('span[itemprop=author]')
        headline_h1 = response.css('h1[itemprop=headline]::text')

        if author_span is not None:
            article_author = author_span.xpath(".//a/span/text()").extract_first()
            author_url = author_span.xpath(".//a/@href").extract_first()

        if headline_h1 is not None:
            headline = headline_h1.extract_first()


        if "/audio/" in article_url:
            article_text_div =  response.css('div[class=content__main-column]')

        elif "/gallery/" in article_url:
            article_text_div =  response.css('div[class=content__main]')
        else:
            article_text_div =  response.css('div[itemprop=articleBody]')

        try:
            if article_text_div is not None:
                soup = BeautifulSoup(article_text_div.extract_first())
                article_text = soup.get_text().strip()
        except:
            print "Exception happened"
        result = self.table.insert_one({"url":article_url, "content":article_text, "title":headline, "author":article_author, "author_link":author_url})
        print('One article: {0}'.format(result.inserted_id))









