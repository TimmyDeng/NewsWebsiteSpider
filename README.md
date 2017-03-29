# NewsWebsiteSpider
This is an application to crawl the online news website using scrapy, e.g. www.theguardian.com/au, parse the html, extract the information and store the information in MangoDB

# Program description 
1. Set mangoDB in NewsWebsiteSpider\newsSpider\newsSpider\spiders\db_setting.py.
2. Set spider request parameters in NewsWebsiteSpider\newsSpider\newsSpider\spiders\config.ini.
3. The code for crawling, parsing the webpage in www.theguardian.com/au and extracting info is in NewsWebsiteSpider\newsSpider\newsSpider\spiders\NewSpider.py, the parsing logics is the sample.
4. Crawler: step1: cd NewsWebsiteSpider\newsSpider and step2(crawl command):scrapy crawl newsSpider, the spider will automatically crawl the website, parse html, extract the infomations and save the articles in mangoDB.
6. Search for articles by keyword: the code is in NewsWebsiteSpider\newsSpider\newsSpider\QueryCMD.py, please use command:python QueryCMD.py and check the commend in the file.
7. The screenshot for the result is under NewsWebsiteSpider\results\screenshots.
