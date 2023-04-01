from ReaderClass import*
from ViewClass import*
from SammlungClass import* 
from ModelClass import*
from GameFinaleClass import*
from ZeitClass import*

class controllerClass(sammlungClass): #Controller Class beinhaltet die Logikstruktur unseres Games
    def __init__(self): #konstruktor
        ###lokale variablen die heufig verwendet werden###
        self.PictureID = 0             #beinhaltet das aktuell gezeigte bild(als Zahl)
        self.TextID = 0                #beinhaltet die stelle des Textes
        self.ItemID = 0                #0: Inventar geschlossen, 1: Inventar geoeffnet, 2: Inventar offen & Item in der Hand
        self.InventarInhalt = 0        #1: 1. Bild im Inventar wird dargestellt / ist iteragierbar...
        self.TuerID = 0                #Variable die die bereits geoeffneten Tueren beinhaltet
        self.KuelschrankOffen = 0      #0 = geschlossen, 1= offen, 2= offen & Hammer im Inv
        self.gameFinale = False         #False: gameFinale wird nicht ausgeloesst, wenn True: dann wird die GameFinale Animation getriggert
        
        ###lokale variablen die nicht so heufig verwendet werden###
        self.wert = 0                           #wert der die PictureID waerend der Textinteraktion steuert
        self.endAnimationControllerWert = 0     #bestimmt den stand der endanimation(den wechsel der Frames)
        self.mouseTextAnzeige = False           #triggert den OverlayText beim Hovern ueber Speichern/Menue buttons
        self.exitAnimation = False              #triggert die animation bei beenden des Spiels
        self.Ratte = 0                          # 0= 
        self.Prof= 0                            # 0= keine reaktion
        self.tastenbelegung = False             #True= Tastenbelegung.png wir angezeigt. False= nicht#
        
        ###Globale Liste###
        self.ItemList = ["t.png","ItemKaese.png","ItemDreher.png","ItemSchluessel.png","t.png", "ItemHammer.png", "ItemMunition.png"]
        
        ###Instanzen verschiedener importierter Klassen, die den zugriff auf deren Funktionen erlaubt(vor Vererbung entstanden)###
        self.view = viewClass()         #Instanz der viewClass mit der verschiedene Funktionen aus der Classe in der Controller Classe ausgefuehrt werden koennen
        self.sammlung = sammlungClass() #""
        self.finale = gameFinaleClass() #""
        self.zeit = zeitClass()         #"" fuer die getter uns setter sowie die private Variable
        
        ###Instanzen der readerClass mit vorgegebenen Uebergapeparametern (Dateinamen)###
        self.savedGame = readerClass("Spielstand.csv")  #liesst die CSV mithilfe der readerClass aus
        self.pList = readerClass("Pictures.csv")        #liesst die CSV mithilfe der readerClass aus
        self.textList = readerClass("Textlist.txt")     #liesst die txt datei mithilfe der readerClass aus & schreibt den Inhalt der Datei in die Liste
        self.personList = readerClass("Personlist.csv") #"" fuer die CSV
      
        
        
        
###Funktionen in der Setup Methode###
    
    def laden(self): #funktion die Bildernamen aus einer CSV datei laed
        self.PictureList = self.pList.lesen()       #liesst die Pitures CSV datei in die liste die alle hintergrundbilder beinhaltet
        self.view.ladeSchriftart("Game12.vlw", 24)  #
        
        

###Funktionen in der Draw Methode###
    
    def buttonBackground(self):  #Funktion die die Farbe der Buttons steuert, wenn die maus darueber schwebt
        if self.PictureID == 0 and self.gameFinale == False:                                                       #
            self.view.rechteck("#0080FF", 0,0,1920,1080,0)                            #
            if self.sammlung.mousePosition(width/3,height/3,width/3,100) == True:     #
                self.view.rechteck("#FFFF00", width/3,height/3,width/3,100,0)         #
            elif self.sammlung.mousePosition(width/3,height/2,width/3,100) == True:   #
                self.view.rechteck("#FFFF00", width/3,height/2,width/3,100,0)         #
            elif self.sammlung.mousePosition(width/3,height/1.5,width/3,100) == True: #
                self.view.rechteck("#FF2000", width/3,height/1.5,width/3,100,0)       #
        else:
            pass
                
    def hintergrundBilder(self): #funktion die das laden der Hintergrundbilder steuer
        if self.gameFinale==False: #wenn das finale nicht aktiv ist
            self.view.pictureCreator(self.PictureList[self.PictureID],0,0,1920,1080) #bezug view,funktion Bilder laden mit (BilderListe(BilderNummer) koordinaten(x,y,l,w))
        if self.tastenbelegung == True and 0< self.PictureID < 13: #wenn die Tastenbelegungs Variable True und der ladescreen (von 1 bis 12 PictureID) aktiv ist
            self.view.pictureCreator("Tastenbelegung.png",0,0,1920,1080)
        else:
            pass
        
    def animationDuration(self): #funktion fuer die Ladeanimation und die Animation waerend des gespraechs mit Prof
        if 0 < self.PictureID < 10 or 10 < self.PictureID < 14: #Bereich in dem die Ladeanimation (0 bis 10)
            if self.sammlung.verzoegerung(12) == True:          #Verzoegerung der ausfuehrung um 0,2s (12/60 sec bei 60fps)
                self.PictureID +=1                              #naechstem Hintergrundbild
        elif self.PictureID == 10:                              #Stelle fuer LadeBild 90% 
            if self.sammlung.verzoegerung(30) == True:          #Verzoegerung der ausfuehrung um 0,5s (30/60 sec bei 60fps)
                self.PictureID +=1                              #naechstem Hintergrundbild
        
                
                
    def indivBilder(self): #funktion die Individuelle Bilder mehrere Interatkionsgegenstaende im Spiel
        if 12< self.PictureID <= 15:                                       #gespraech mit Prof
            if self.TextID == 0:   
                self.view.pictureCreator("Prof.png", 150, 325, 1260, 720)  #
                self.view.pictureCreator("Lab2.png", 0,0,1920,1080)        #
                self.view.pictureCreator("EBlase.png", 900, 300, 412, 220)  # 
            

            elif 0 < self.TextID < 11 or 26 < self.TextID < 46 and self.PictureID < 15: #laed Prolog Text und weiter Pfeil wenn im Prolog und nicht der Mond auf die Erde Animation aktiv
                self.view.pictureCreator("Prof.png", 150, 325, 1260, 720)               #
                self.view.pictureCreator("Lab2.png", 0,0,1920,1080)                     #
                self.view.rechteck("#F0E68C", 10,900,1900,120,10)                       #hintergrund des Textes
                self.TextL = self.textList.lesen()                                      #
                self.PersonL = self.personList.lesen()                                  #
                self.view.createText(self.TextID, self.TextL, self.PersonL)             #
                self.view.pictureCreator("Pfeil2.png", 1830,922,80,80)                   #
            
            elif 10 < self.TextID < 27:                          # wenn die Mond faellt auf Erde Animation aktiv
                self.view.rechteck("#F0E68C", 10,900,1900,120,10)            #hintergrund des Textes
                self.TextL = self.textList.lesen()                           #
                self.PersonL = self.personList.lesen()                       #
                self.view.createText(self.TextID, self.TextL, self.PersonL)  #
                self.view.pictureCreator("Pfeil2.png", 1830,922,80,80)       #
            
            elif self.TextID >= 46:                                      #zeigt den Prof nach Text und Animation an             
                self.view.pictureCreator("Prof.png", 150, 325, 1260, 720)#
                self.view.pictureCreator("Lab2.png", 0,0,1920,1080)      #
    
        elif self.PictureID == 19:                                            #Hammer in kuelschrank anzeige
            if self.KuelschrankOffen == 1:                                    #kuelschrank offen und hammer darin
                self.view.pictureCreator("Hammer.png",*itemDic["Hammer.png"]) #
        else:
            pass #end 
                 
                
    def overlay(self):                 #funktion fuer unser Overlay im Spiel
        if 14 < self.PictureID < 22:               #bedingung: PicID muss nach dem Prolog sein um das Overlay zu sehen und zu bearbeiten
            if 14< self.PictureID < 22:            #alle bereiche (Hintergrundbilder) nach dem Labor 1 mit Prof (PictureID 15)
                
                if self.sammlung.mousePosition(1800,25, 80,80) == True:                  #Spiel Speichern Text
                    self.view.mouseText("Spiel Speichern",1830,60,340,290,40,0,0,0)      #
                elif self.sammlung.mousePosition(1800,120, 80,80) == True:               #Hauptmenue Text
                    self.view.mouseText("Hauptmenue",1840,160,270,215,40, 0,0,0)         #
                    
                if self.PictureID == 15: 
                    self.view.pictureCreator("WeiterButton.png", 1800,500,120,120)
                    
                if 15 < self.PictureID < 22:
                    self.view.pictureCreator("ZurueckButton.png",10,500,120,120)
                    if 15< self.PictureID <= 17 and self.TuerID == 0:                     #erster Raum
                        self.view.pictureCreator("WeiterButton.png", 1800,500,120,120)    #
                    elif 15< self.PictureID <= 19 and self.TuerID >=1:                    #tuer 1
                        self.view.pictureCreator("WeiterButton.png", 1800,500,120,120)    #
                    elif 15< self.PictureID <= 20 and self.TuerID == 2:                   #tuer 2
                        self.view.pictureCreator("WeiterButton.png", 1800,500,120,120)    #
            
                
            if self.ItemID >0:                                                                                          #wenn Inv geoeffnet, oder item in hand
                self.view.pictureCreator("Inventar.png", 0,0,1920,1080)                                                 # 
                self.sammlung.bilderErstellen(self.ItemList[self.InventarInhalt], *itemDic[self.ItemList[self.InventarInhalt]])    #
                
                
            else: 
                self.view.pictureCreator("Overlay.png", 0,0,1920,1080)
                cursor()
                if self.mouseTextAnzeige == True:
                    self.view.rechteck("#FFFFFF", width/2-198,height/2-28,198*2,18*2+8,1)
                    self.view.normalText("Spiel gespeichert","#00003C", width/2-188,height/2+8,30)
                    
                    if self.sammlung.verzoegerung(10) == True:
                        self.mouseTextAnzeige = False
    
    def moonAnimation(self): #funktion die beim beenden des spiels die Mond sequenz abspielt
        if self.exitAnimation == True and self.gameFinale == False: #
            self.view.ladeSchriftart("TNRB.vlw", 75)
            self.view.mouseText("\(^_^)/",mouseX,mouseY,112,0,0, random(0,255),random(0,255),random(0,255)) #funny 
            #noCursor()
            if 192 < self.PictureID < 199:
                if self.sammlung.verzoegerung(10) == True:
                    self.PictureID += 1                    #
            elif self.PictureID == 199:
                if self.sammlung.verzoegerung(12) == True:
                    exit()
                    
                
    def textAnimation(self):
        if 10< self.TextID <18:
            self.view.pictureCreator("Teilchenbeschleuniger.png",0,0,1920,1080)
        elif 17< self.TextID <19:
            self.wert = 193
            self.view.pictureCreator(self.PictureList[self.wert],0,0,1920,1080)
        elif 18< self.TextID < 27:
            self.view.pictureCreator(self.PictureList[self.wert],0,0,1920,1080)
            if self.sammlung.verzoegerung(6) == True:
                if self.wert == 199:
                    self.wert = 192
                self.wert +=1
                
    def inHandBilder(self):  #Controller der die Bilder in der Hand darstellt
        imageMode(CENTER)    #Zentiert das bild mittig von der maus 
        if self.ItemID == 2: #
            #noCursor()
            self.view.pictureCreator(self.ItemList[self.InventarInhalt],mouseX,mouseY,200,200)
        imageMode(CORNER) 

    def reactionNPC(self):  #reaktionen der NPCs auf interaktion
        if self.Ratte == 2:
            self.view.normalText("Ohh danke, hier hast du diesen Schrauber, den du Suchst.","#0A0A0A",1000,650,20)
            self.view.normalText("|","#0A0A0A",1200,700,40)
            if self.sammlung.verzoegerung(30) == True:
                self.Ratte = 0
                
        elif self.Ratte == 1: #wenn 1
            self.view.normalText("Was soll ich denn damit??? Ich habe ja nichtmal Daumen ;(","#0A0A0A",1000,650,20)
            self.view.normalText("|","#0A0A0A",1200,700,40)
            if self.sammlung.verzoegerung(30) == True:
                self.Ratte = 0
                
        if self.Prof== 2:
            self.view.normalText("Uiii, Suupiii, genau den Habe ich gesucht! Hier der Schluessel fuer Tuer 1.","#0A0A0A",500,350,18)
            self.view.normalText("|","#0A0A0A",715,400,40)
            if self.sammlung.verzoegerung(30) == True:
                self.Prof = 0
                
        elif self.Prof== 1:
            self.view.normalText("Wie soll denn dass bitte HELFEN???","#0A0A0A",500,350,18)
            self.view.normalText("|","#0A0A0A",715,400,40)
            if self.sammlung.verzoegerung(30) == True:
                self.Prof = 0
                
        elif self.Prof== 3:
            self.view.normalText("Super, jetzt haben wir alles!!!","#0A0A0A",500,350,18)
            self.view.normalText("|","#0A0A0A",715,400,40)
            if self.sammlung.verzoegerung(30) == True:
                self.Prof = 0
                self.PictureID = 23
                self.gameFinale=True #triggert die endanimation des Games
            
    def gameFinaleAnimation(self): #controllfunktion die den ablauf der endanimation steuert
        if self.gameFinale == True: #wenn die endanimation getriggert wird, dann
            if self.endAnimationControllerWert == 0: #wenn die Variable "0" ist, dann
                if self.finale.frame1() == next:     #wenn frame1 "next" returnt, dann
                    self.endAnimationControllerWert += 1  #wird die endAnimationControllerWert Variable +1 addiert
                    
            elif self.endAnimationControllerWert == 1: #wenn endAnimationControllerWert = 1, dann
                self.finale.frame2() #wird frame2 aus der GameFinalClass ausgefuehrt
                if self.sammlung.verzoegerung(5) == True: #nach einer verzoegerung von 5/60 sekunden
                    self.endAnimationControllerWert += 1 #""
            
            elif self.endAnimationControllerWert == 2: #""
                self.finale.frame3() #""
                if self.sammlung.verzoegerung(10) == True: #"" nach 10/60 sekunden
                    self.endAnimationControllerWert += 1 #""
            
            elif self.endAnimationControllerWert == 3: #""
                self.finale.frame4() #""
                if self.sammlung.verzoegerung(7) == True: #"" nach 7/60 sekunden
                    self.endAnimationControllerWert += 1 #""
                    
            elif self.endAnimationControllerWert == 4: #""
                self.finale.frame5() #""
                if self.sammlung.verzoegerung(240) == True: #""
                    self.endAnimationControllerWert += 1 #""
                    
            elif self.endAnimationControllerWert == 5: #""
                self.finale.frame6() #""
                if self.sammlung.verzoegerung(420) == True: #""
                    self.endAnimationControllerWert += 1 #""
                
            elif self.endAnimationControllerWert == 6:  #""
                if self.finale.frame7() == "ende":   #wenn frame7 "ende" returnt, dann
                    self.PictureID = 0             #beinhaltet das aktuell gezeigte bild(als Zahl)
                    self.TextID = 0                #beinhaltet die stelle des Textes
                    self.ItemID = 0                #0: Inventar geschlossen, 1: Inventar geoeffnet, 2: Inventar offen & Item in der Hand
                    self.InventarInhalt = 0        #1: 1. Bild im Inventar wird dargestellt / ist iteragierbar...
                    self.TuerID = 0                #Variable die die bereits geoeffneten Tueren beinhaltet
                    self.KuelschrankOffen = 0      #0 = geschlossen, 1= offen, 2= offen & Hammer im Inv
                    self.gameFinale = False        #False: gameFinale wird nicht ausgeloesst, wenn True: dann wird die GameFinale Animation getriggert
    
    def menueZeit(self):
        if self.PictureID == 0:
            self.zeit.zeitSetzer()
            self.view.normalText(self.zeit.zeitGeber(),"#FFFFFF",1580,120,45)

                
                
###Funktionen in der mouseClicked Methode###
        
    def startMenueButtons(self): #Funktion die die Interaktion mit den Buttons abfragt
        if self.PictureID == 0:                                                     #wenn wir uns im startscreen befinden 
            if self.sammlung.mousePosition(width/3,height/3,width/3,100) == True:   #Neues Spiel
                self.InventarInhalt = 1      #gibt Spieler Starterkaese
                self.PictureID = 1           #startet die Ladeanimation
                self.TextID = 0              #resettet das Gespraech mit Prof
                self.ItemID = 0              #schliesst Inventar
                self.tastenbelegung = True   #zeigt dann die Tastenbelegung an True= Tastenbelegung.pnh
            elif self.sammlung.mousePosition(width/3,height/2,width/3,100) == True: #Altes Spiel laden
                self.TextID = 46                                      #ID wird auf 46 gesetzt (kein Text mehr)
                self.PictureID = self.savedGame.lesen()[0]            #
                self.InvantarInhalt = self.savedGame.lesen()[1]       #
                self.ItemID = self.savedGame.lesen()[2]               #funktion die Die Spielstand datei laed
                self.TuerID = self.savedGame.lesen()[3]               #
                self.KuelschrankOffen = self.savedGame.lesen()[4]     #
                if self.KuelschrankOffen == True:                      #wenn kuelschrank offen ist, dann
                    self.PictureList.remove("Kueche.png")                #entferne das Kueche.png aus der PictureList
                    self.PictureList.insert(19,"KuecheOffen.png")        #und ersetzt es mit dem KuecheOffen.png
            
            elif self.sammlung.mousePosition(width/3,height/1.5,width/3,100) == True: #Spiel Beenden Button gedrueckt
                self.exitAnimation = True      #setzt die "exitAnimation" wenn das Game Beendet wird auf true 
                self.PictureID = 193           #und laedt das ende 
            
    def interaktionText(self): # Funktion fuer die Textineraktion mit Sprechblase und weiter Pfeil fuer den Text
        if self.PictureID == 14:                                                                #Picture IDs fuer das Labor mit prof 
            if self.sammlung.mousePosition(900, 300, 400, 300) == True and self.TextID == 0:    #Sprechblase 1. Klick um TextID auf 1 zu setzen
                self.TextID = self.TextID + 1                                                   #Startet den prolog 
            elif self.sammlung.mousePosition(1835,922,80,80) == True and 0 < self.TextID < 46 : #Weiter Button fuer Sprechen mit Prof 
                self.TextID = self.TextID + 1                                                   #wird StoryTextId um 1 addiert
                if self.TextID == 45:                                                           #
                    self.InventarInhalt = 1                                                     #Gibt dem Spieler den Kaese
                elif self.TextID == 46:                                                         #wenn er zuende geredet hat
                    self.PictureID = 15                                                         #lade das labor 
            
                    
    def interaktionRaum(self):               #kontrolliert die buttons die zur navigation der Raeme dient
        if 14 < self.PictureID < 22:                                   #bereich der Hintergrundbilder overlay aktiv
            if self.sammlung.mousePosition(1800,500,120,120) == True:  #weiter button Bilder
                self.Ratte = 0                                         #setzt wert auf 0, damit reaktionstext nicht mehr angezeigt wird
                self.Prof = 0                                          #""
                if 14< self.PictureID <= 17 and self.TuerID == 0:      #Raum weiter wenn kein schluessel 
                        self.PictureID = self.PictureID+1              #
                elif 14< self.PictureID <= 19 and self.TuerID >= 1:    #Raum weiter wenn 1. schluessel 
                        self.PictureID +=1 
                elif 14< self.PictureID <= 21 and self.TuerID == 2:    #Raum weiter wenn 2. schluessel 
                        self.PictureID +=1                             #
                        
            elif self.sammlung.mousePosition(10,500,120,120) == True:  #zurueck button Bilder
                self.Ratte = 0                                         #setzt wert auf 0, damit reaktionstext nicht mehr angezeigt wird
                self.Prof = 0                                          #""
                if 15 < self.PictureID < 22:                           #
                    self.PictureID -=1                                 #
                
                
    def overlayInteraktion(self):#fuer interation mit inventar
        if 14 < self.PictureID < 22: 
            if self.ItemID == 0 :
                if self.sammlung.mousePosition(1740,940, 100,80) == True: #oeffnet Inventar
                    self.ItemID = 1
                    print("#oeffnet Inventar",self.ItemID)
                elif self.sammlung.mousePosition(1800,25, 80,80) == True: #Spiel Speichern knopf
                    self.sammlung.spielSpeichern(self.PictureID,self.InventarInhalt,self.ItemID,self.TuerID, self.KuelschrankOffen)
                    self.mouseTextAnzeige = True
                    print("Spiel gespeichert mit |PictureID:",self.PictureID,"| InventarInhalt:",self.InventarInhalt," = ",self.ItemList[self.InventarInhalt],"| ItemID:",self.ItemID,"| TuerID:", self.TuerID,"| KuelschrankOffen:", self.KuelschrankOffen,"|")
                    
                elif self.sammlung.mousePosition(1800,120, 80,80) == True: #Zurueck zum Hauptmenue
                    self.PictureID = 0
                    
            elif self.ItemID > 0: #wenn Inventar geoeffnet
                if self.sammlung.mousePosition(1740,940, 100,80) == True: #inv schliessen button
                    self.ItemID = 0 #inv geschlossen
                    
                ###Funktion die Items wieder ins Inv zurueck zu legen###
                elif self.sammlung.mousePosition(*itemDic[self.ItemList[self.InventarInhalt]]) == True: #erster Inventarslot von links
                    self.ItemID = self.sammlung.inUndAusHand(self.ItemID) #self.ItemID: ob item in hand oder nicht 

                                    
    def gibMirItemAbfrage(self):# nur als test funktion fuer die interaktion mit der ratte
        
        if self.PictureID == 16:                                 #Abfrage fuer die Ratte 
            if self.sammlung.mousePosition(1109,730,235,280):    #Ratte position
                if self.InventarInhalt == 1 and self.ItemID == 2:#Ratte mit Kaese
                    self.InventarInhalt = 2                      #   
                    self.ItemID = 1                              #Simuliert die interaktion mit der maus,schliesst inventar,setzt in der funktion interaktionRaum(self): den Mous
                    self.Ratte = 2                               #triggert den Text fuer Maus 2: Ohh danke, hier bekommst du diesen Schrauber
                    
                else:
                    self.Ratte = 1  #Triggert Text 1: Was soll ich denn mit einem Schrauber??? Ich habe ja nichtmal daumen ;(
                    self.ItemID = 1 #
                
        elif self.PictureID == 15: #Abfrage fuer den Prof 
            if self.sammlung.mousePosition(480, 425,600, 500):        #Prof Position mous anklick interaktion 
                if self.InventarInhalt == 2 and self.ItemID == 2:     #wenn wir den schraubendreher haben & das inventar offen ist
                    self.InventarInhalt = 3                           #wir bekommen hier den schluessel
                    self.ItemID = 1                                   #Inventar soll offen bleiben 
                    self.Prof = 2                                     #text vom prof...
                elif self.InventarInhalt == 6 and self.ItemID == 2:   #fragt ab ob Inventarinhalt 6 ist und Inventar offen ist?
                    self.ItemID = 1                                   #
                    self.InventarInhalt = 4                           #leeres PNG
                    self.Prof = 3                                     #
                else:
                    self.Prof = 1                                     #
                    self.ItemID = 1                                   #
                
                
        elif self.PictureID == 18: #abfrage tuer 1
            if self.sammlung.mousePosition(400,100,1120,800) and self.InventarInhalt == 3 and self.ItemID == 2:
               self.InventarInhalt = 4
               self.TuerID = 1
               self.ItemID = 1
               
        elif self.PictureID == 20: #abfrage tuer 2
            if self.sammlung.mousePosition(400,100,1120,800) and self.InventarInhalt == 5 and self.ItemID == 2:
               self.InventarInhalt = 4
               self.TuerID = 2
               self.ItemID = 1 
               
        elif self.PictureID == 21: #abfrage um dem spieler die Monition zu geben
             if self.sammlung.mousePosition(1330,445,200,200):
                 self.InventarInhalt = 6
                 self.ItemID = 1
                
               
            
    def kuelschrankoeffnen(self):
        if self.PictureID == 19: #wenn keulschrank bild angezeigt wird
            if self.KuelschrankOffen == 0 and self.sammlung.mousePosition(130,118, 350, 645): #wenn kuelschrankg zu + Auf kuelschrak geklickt
                if self.sammlung.mousePosition(130,118, 350, 645):
                    print(self.PictureList)
                    self.PictureList.remove("Kueche.png")
                    self.PictureList.insert(19,"KuecheOffen.png")
                    print(self.PictureList)
                    self.KuelschrankOffen = 1 #kuelschrank offen
                    
            elif self.KuelschrankOffen == 1 and self.sammlung.mousePosition(130,410,100,120) == True: #wenn kuelschrankg offen + Hammer geklickt
                self.InventarInhalt = 5
                self.KuelschrankOffen = 2
                self.ItemID = 1
                print("Hammer im inv")
                
                

            
###Funktionen in der keyPressed Methode###

    def tastaturInteraktion(self): #funktion die die Tastaturinteraktion ermoeglicht
        
        if key == 'e' or key == 'E':   #wenn Key auf Tastatur "e" /"E" gedrueckt wird und alles darunter auch zutrifft, dann soll die TextID +1 gerechnet werden
            if self.PictureID == 14 and self.TextID < 1: 
                self.TextID +=1
    
        elif key== 'd' or key == 'D' or keyCode == 39: #keyCode 39 = pfeiltaste rechts
            if self.PictureID == 14 and 0 < self.TextID < 46: #im gespraech mit Prof
                self.TextID = self.TextID+1
                if self.TextID == 46:
                    self.PictureID = 15
            elif 14< self.PictureID <= 17 and self.TuerID == 0:    #Raum weiter wenn kein schluessel 
                self.PictureID +=1                                 #
            elif 14< self.PictureID <= 19 and self.TuerID >= 1:    #Raum weiter wenn 1. schluessel 
                self.PictureID +=1                                 #
            elif 14< self.PictureID <= 20 and self.TuerID == 2:    #Raum weiter wenn 2. schluessel 
                self.PictureID +=1                                 #
                
        elif key== 'a' or key == 'A' or keyCode == 37: #Raum zurueck
            if 15 < self.PictureID < 30:                          #
                    self.PictureID -=1
                    
        elif key== 'i' or key == 'I': #press i to open/close Inventory
            if self.ItemID == 0:
                self.ItemID = 1 
            else:
                self.ItemID = 0
                
        elif keyCode == 32: #wenn SPACE gedrueckt
            if 0< self.PictureID < 14:
                self.tastenbelegung = False
                
