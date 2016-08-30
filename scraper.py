from collections import Counter
import feedparser

feedUrls = [ "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml" ]
feeds = []

def downloadFeeds():
    for feedUrl in feedUrls:
        print "Parsing feed" , feedUrl
        rssData = feedparser.parse( feedUrl )

        feed = Feed( feedUrl )

        for item in rssData['items']:
            title = item['title']
            feed.addTitle( title )

        feeds.append(feed)

    return feeds
    
# Feed class
class Feed:
    def __init__(self, feedUrl):
        self.feedUrl = feedUrl
        self.titles = []

    def addTitle(self, title):
        self.titles.append(title)
