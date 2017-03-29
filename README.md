# NewsWebsiteSpider
This is an application to crawl the online news website using scrapy, e.g. www.theguardian.com/au
#######################################################\n
Program description 
Set mangoDB in NewsWebsiteSpider\newsSpider\newsSpider\spiders\db_setting.py
Set spider request parameters in NewsWebsiteSpider\newsSpider\newsSpider\spiders\config.ini
The code for crawling, parsing the webpage in www.theguardian.com/au and extracting info is in NewsWebsiteSpider\newsSpider\newsSpider\spiders\NewSpider.py, the parsing logics is the sample.
Crawler: step1: cd NewsWebsiteSpider\newsSpider step2(crawl command):scrapy crawl newsSpider, the spider will automatically crawl the website and save the articles in mangoDB
Search for articles by keyword: the code is in NewsWebsiteSpider\newsSpider\newsSpider\QueryCMD.py, please use command:python QueryCMD.py and check the commend in the file
The screenshot for the result is under NewsWebsiteSpider\results\screenshots
