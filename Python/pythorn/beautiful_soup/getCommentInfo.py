import urllib
from bs4 import BeautifulSoup

# from mylog import MyLog as mylog

print(urllib)
print(BeautifulSoup)


class Item(object):
    title = None
    firstAuthor = None
    firstTime = None
    reNum = None
    content = None
    lastAuthor = None
    lastTime = None


print(Item)


class GetTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        # self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self, pageSum):
        urls = []
        pns = [str(i * 50) for i in range(pageSum)]

        ul = self.url.split('=')
