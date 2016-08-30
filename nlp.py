import nltk

def getImportantTitleWords(feeds):
    
    stopwords = nltk.corpus.stopwords.words('english')

    importantTitleWords = []

    for feed in feeds:
        for title in feed.titles:
            lowerCaseWords = [ x.lower() for x in nltk.word_tokenize( title ) if len(x) > 1 ]
            lowerCaseImportantWords = [ x for x in lowerCaseWords if not x in stopwords ]
            importantTitleWords.extend( lowerCaseImportantWords )

    return importantTitleWords 
