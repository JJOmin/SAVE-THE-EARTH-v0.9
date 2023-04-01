import os #importieren das os modul
class readerClass(object):
    FileName = ""
    def __init__(self, aFileName): #konstruktor der Klasse
        self.FileName = aFileName #bestimmung der variablen
    
    def schreiben(self, writeList = []):
        try:
            with open(self.FileName, "w") as listFile:
                for listItem in writeList:
                    listFile.write('%s\n' % listItem)
        except IOError:
            print("Die Datei:",aFileName," wurde nicht gefunden!")
    
    def lesen(self):
        list = []
        try:
            with open(self.FileName, "r") as listFile:
                for line in listFile:
                    # Zeilenumbruch entfernen
                    currentString = line[:-1]
                    if currentString.isdigit():
                        list.append(int(currentString))
                    else:
                        list.append(currentString)
        except IOError:
            print("Datei %s wurde nicht gefunden" % (self.FileName))
        return list
