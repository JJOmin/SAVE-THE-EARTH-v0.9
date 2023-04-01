from ReaderClass import*
from ViewClass import*
from ModelClass import*

class sammlungClass(): # uebergeordnete classe 
    
    def __init__(self):
        self.spielstandList = readerClass("Spielstand.csv")
        self.view = viewClass() #Instanz der viewClass
        self.x = 0  #hilfswariabl fuer die verzuegerung() 
        
        
    ###Controller Funktionen###    
    def mousePosition(self, x1,y1,l,w): #x1,y1: X,Y Koordinaten, l,w: length & width (laenge & breite)
        if x1 < mouseX < x1+l and y1 < mouseY < y1+w: #abfrage ob die der Bereich der Uebergabeparameter mit der Pos der Maus uebereinstimmt
            self.mausAbfrage = True
            return self.mausAbfrage
        else: 
            self.mausAbfrage = False
            return self.mausAbfrage
        
    ###Speicher funktion####    
    def spielSpeichern(self,PictureID, TextID, ItemID, TuerID, KuelschrankOffen): #funktion die den aktuellen Spielstand (PictureID, TextID, ItemID) in die "Spielstand.csv" speichert
        self.spielstandList.schreiben([PictureID, TextID, ItemID, TuerID, KuelschrankOffen])
        
    def verzoegerung(self, ende):
        self.x = self.x+1
        if self.x == ende:
            self.x = 0
            return True
        else:
            return False
    

    def bilderErstellen(self, Name, pos_x,pos_y,l,w): #funktion die Bilder erstellt
        self.view.pictureCreator(Name,pos_x,pos_y,l,w)
        
    def inUndAusHand(self, ItemID): #funktion die Items wieder ins Inventar legt (fuer ItemID 1 & 2)
        if ItemID == 1: #wenn ItemID 1 ist (Inv nur Offen) und wenn Inventar Inhalt = 1 ist (nur Kaese im Inv)
            return 2 #legt Item von Inv slot 1 in die Hand
        elif ItemID == 2: #wenn Item in Hand
            cursor()
            return 1 #legt Item von Inv slot 1 zurueck ins Inventar
            
            
            
    ###Animationen / View Controllstrukturen###
   
    def tryUndExcept(self):  #funktion die hilft wenn der InventarInhalt wert ueber dem Inhalt der Liste ist
        try:
            simulationswert = self.ItemList[self.InventarInhalt]               #weil self.InventarInhalt=Entwas was nicht in self.ItemList enthalten ist
        except IndexError:
            print("Das angeforderte Item:",str(self.InventarInhalt)+"ist nicht in der ItemList vorhanden.")#Nur zum demonstrieren das es.        
