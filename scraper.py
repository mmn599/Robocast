from collections import Counter
import feedparser
import nltk

feeds = [ "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml" ]

titleWords = []
wordFreq = {}

for feed in feeds:
    print "Parsing feed..."
    rssData = feedparser.parse( feed )
    for item in rssData['items']:
        title = item['title']
        lowerWords = [ x.lower() for x in nltk.word_tokenize( title ) if len(x) > 1 ]
        for word in lowerWords:
            if word in wordFreq:
                wordFreq[ word ] = wordFreq[ word ] + 1
            else:
                wordFreq[ word ] = 1
        titleWords.extend( lowerWords )

def getTitleWords():
    return titleWords

def getWordFrequencies():
    return Counter(titleWords)
