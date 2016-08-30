import nlp
import scraper 

feeds = scraper.downloadFeeds()
importantTitleWords = nlp.getImportantTitleWords( feeds )

for word in importantTitleWords:
    print word

