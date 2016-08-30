scriptFilename = "script.txt"
aiffFilename = "output.aiff"
mp3Filename = "output.mp3"

noFileCommand = "say -f " + scriptFilename

sayCommand = "say -f " + scriptFilename + " -o " + aiffFilename
mp3Command = "lame -m m " + aiffFilename + " " + mp3Filename

#system(sayCommand + ";" + mp3Command)
system(noFileCommand)
