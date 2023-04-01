from ViewClass import*
from SammlungClass import*

class gameFinaleClass():
    def __init__(self): #konstruktor
        self.x_ende = 0.1000            #X position des Mondes
        self.y_ende = 0.1000            #Y position des Mondes
        self.a = 0.0                    #Bestimmt den abstand der kreise des sin zur y-Achse, bezugswert fuer den sinus 
        self.n = True                   #Hilfsvariable um getimte Animationen zu triggern (z.B. Hintergrundsterne 1mal generieren um Systemlast zu sparen)
        self.inc = (TWO_PI/90)+1        #Phasenverschiebung zum Vorherigen punkt
        self.inc2 = (TWO_PI/10)-2       #Phasenverschiebung zum Vorherigen punkt
        self.abspann = 0                #Hilfsvariable die den Text vom Porf steuert
        self.view = viewClass()         #Bezug auf ViewClass 
        self.sammlung = sammlungClass() #Bezug auf SammmlungClass
            
    def frame1(self): #Endanimation Mond faellt auf Erde
        self.view.pictureCreator("Erde.png", 0,0,1920,1080) #erstellt Bild "Erde.png" an gegebenen koordinaten mit gegebenem abstand zu den Koordinaten
        self.view.pictureCreator("Moon.png", self.x_ende,self.y_ende,1920,1080) 
        self.view.pictureCreator("Prof2.png", 550, 275, 200, 114)
        self.view.pictureCreator("SinusP.png", 520,320,130,61)
        self.view.pictureCreator("ItemMunition.png", 680,300,50,50)
        
        if self.x_ende < 220:      #bis auf 220 von x_ende soll der Mond fallen
            self.x_ende = self.x_ende+7*float(18/9)  #x_ende wird mit 7*18/9 addiert wegen dem seittenverhaeltnis 16/9
            self.y_ende = self.y_ende+7*float(18/16) #y_ende wird mit 7*18/16 addiert
        else:
            return next

                    
    def frame2(self):
        self.view.pictureCreator("Erde.png", 0,0,5000,2812.5) #herrangezoomte erde wird dargestellt
        
    def frame3(self): #waffe wird geladen
        self.view.pictureCreator("Erde.png", 0,0,5000,2812.5) #herrangezoomte erde
        self.view.pictureCreator("SinusP.png", 200,205,1200,564)
        self.view.pictureCreator("ItemMunition.png", 980,300,400,400)
        
    def frame4(self): #waffe geladen
        self.view.pictureCreator("Erde.png", 0,0,5000,2812.5) #herrangezoomte erde
        self.view.pictureCreator("SinusP.png", 990,205,1200,564)
        
    
    def frame5(self): #Waffe wird ausgefuehrt
        fill("#27245F")      #selbes blau wie hintergrund
        noStroke()           #entfernt Umrandung des rechtecks
        rect(0,300,1010,200) #rechteck hinter dem Lazzer
        fill("#FFFF00")      #frabe des Lazzers
        
        for i in range(1, 1000, 3):  #for schleife fuer den Lazzer fuer den bereich von 1 bis 1000 in abstaenden von 3 zueinander dargestellt,
            circle(i,400+sin(self.a)*80, 10) #kries wird fuer x mit i und fuer y mit: 400+sin(self.a)*80: sellt die winkelverschiebung der Sinuswelle von 0 auf etwa 30 Grad dar und +400 um im auf der y achse im bild zu sein
            self.a = self.a + self.inc #hier wird die vorherige Phase self.a mit dem Phasenversatzwinkel self.inc (increments) addiert, um eine Phasenverschiebung zu erreichen
            
        if self.n == True:  #erstellt die sterne 1 mal und dann nie wieder 
            background("#27245F") #hintergrundfarbe vom Himmel
            for x in range(50):
                fill("#FFFF00")
                circle(random(0,1920),random(0,1080),random(5,15))
                
                fill(20,30,255)
                circle(random(0,1920),random(0,1080),random(5,15))
                x+=1
                self.view.pictureCreator("SinusP.png", 990,205,1200,564)
                
                if x == 50: #nach 50 ausfuehrungen
                    self.n = False
    
    def frame6(self): #Endanimation Mond faellt auf Erde
        fill(25, 39, 99)
        noStroke()
        rect(50,75,420,290)
        fill(0,255,255)
        if self.n == False:
            self.view.pictureCreator("Erde.png", 0,0,1920,1080)
            self.view.pictureCreator("Gun30.png", 450,310,200,200)
            self.n = True
        
        #self.view.pictureCreator("Gun30.png", 520,320,200,200)         ####muss noch bearbeitet werden
        fill("#FFFF00") #frabe des Lazzers
        for i in range(60, 460, 3):
            circle(i,i*6/10+60+sin(self.a)*20, 4)
            self.a = self.a + self.inc2
            
        
        fill(25, 39, 99)
        rect(50,75,100+self.x_ende,100+self.y_ende)
        self.view.pictureCreator("Moon4.png", self.x_ende,self.y_ende,300,300) 
        
        
        if self.x_ende > 10:      #bis auf 220 von x_ende soll der Mond fallen
            self.x_ende = self.x_ende-float(18/9)
            self.y_ende = self.y_ende-float(18/16)
            print(self.x_ende,self.y_ende)
    
    def frame7(self):
        self.view.pictureCreator("Erde.png", -1000,-50,5000,2812.5) #herrangezoomte erde
        self.view.pictureCreator("Prof2.png", 550, 275, 600, 342)
        print(self.abspann)
        if self.sammlung.verzoegerung(20) == True:
            self.abspann +=1 
        if self.abspann == 0:
            self.view.normalText("Grossartig, wir haben es geschafft.","#FFFFFF",600,250,30)
        elif self.abspann == 1:
            self.view.normalText("Ich bin dir zu grossem dank verpflichtet!!!","#FFFFFF",600,250,30)
        elif self.abspann == 2:
            self.view.normalText("Aufwiedersehen und hoffentlich bis bald :)","#FFFFFF",600,250,30)
        elif self.abspann == 3:
            return "ende"
        
        

        
        
        
                    
