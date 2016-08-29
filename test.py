import pandas
from os import system
import scraper 
import operator
import matplotlib.pyplot as plt

frequencies = scraper.getWordFrequencies()

for key, value in frequencies.iteritems():
    print key, value

highestFrequencies = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

words = [ x[0] for x in highestFrequencies ]
freqs = [ x[1] for x in highestFrequencies ]

topWords = words[0:10]
topFreqs = freqs[0:10]

plt.bar(range(len(topFreqs)), topFreqs, align='center')
plt.xticks(range(len(topFreqs)), topWords, size='small')
#plt.show()

scriptFilename = "script.txt"
aiffFilename = "output.aiff"
mp3Filename = "output.mp3"

noFileCommand = "say -f " + scriptFilename

sayCommand = "say -f " + scriptFilename + " -o " + aiffFilename
mp3Command = "lame -m m " + aiffFilename + " " + mp3Filename

#system(sayCommand + ";" + mp3Command)
system(noFileCommand)
