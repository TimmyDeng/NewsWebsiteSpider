import spiders.db_setting as db_setting
from pymongo import MongoClient

def queryArticleByURL(url):
    client = MongoClient(db_setting.db_host, db_setting.db_port)
    db = client[db_setting.db_store]
    table = db[db_setting.db_table]
    article = table.find_one({'url':url})
    if article:
        print "The content for %s is %s"%(url, article['content'])
    else:
        print "The content for %s doesn't exist."%url

def findArticlesByKeywords(keyword):
    client = MongoClient(db_setting.db_host, db_setting.db_port)
    db = client[db_setting.db_store]
    table = db[db_setting.db_table]
    table.create_index([('content','text')])
    articles = table.find({"$text": {"$search": keyword}})
    res_count = articles.count()
    if res_count == 0:
        print "No articles found for keyword %s"%keyword
    else:
        print "Totally %d articles found for keyword %s, Below is the list"%(res_count, keyword)
        idx = 0
        for article in articles:
            idx = idx + 1
            print "*******************************************"
            print("Article #id: %d"%idx)
            print("title: %s"%article['title'])
            print("content: %s"%article['content'])
            print "*******************************************"
if __name__ == "__main__":
    print "Welcome to Query tools for article store"
    while 1:
        print "============================="
        print "Query tools for article store"
        print "1 for query article content by url"
        print "2 for search article by keyword"
        print "3 for exist"
        print "============================="
        choice = input("Please input your choice: ")
        if 1 == choice:
            url = raw_input("Please input the url of article that you want to find: ")
            queryArticleByURL(url)
        elif 2 == choice:
            keyword = raw_input("Please input the keyword that you want to search: ")
            findArticlesByKeywords(keyword)
        elif 3 == choice:
            exit(0)
        else:
          print("Invalid Choice, please try again.")

