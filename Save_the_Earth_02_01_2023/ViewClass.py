
class viewClass():
    def __init__(self):
        self.x = 1 #
        
    def pictureCreator(self,bilderName,pos_x,pos_y,l,w): #funktion die nur bilder laed
        self.img = loadImage(bilderName) #
        image(self.img,pos_x,pos_y,l,w)  #
        
    def rechteck(self, farbe, pos_x,pos_y,l,w,r): #funktion die ein rechteck generieren kann
        strokeWeight(3)
        fill(farbe)
        rect(pos_x,pos_y,l,w,r)
        
    def createText(self, TextID, textL, personL): #ertellt den ProglogText
        self.font = loadFont("Game12.vlw") #bestimmt die Schriftart des Games
        textFont(self.font,25)
        if personL[TextID] == "Prof. X: ": #bestimmt die Farbe vom Text
            fill(102, 153, 0)
        else:
            fill(0, 102, 153) #farbe der schrift 
        text(personL[TextID]+textL[TextID], 30, 970)
        
    def normalText(self, txt,farbe, x,y,xysize): #funktion fuer normalen Text
        textMode(CENTER) #textausrichtung
        fill(farbe)      #textfarbe
        textSize(xysize) #textgruesse
        text(txt,x,y)    #text
        textSize(24)     #setzt Textgruesse zurueck
        textMode(CORNER) #setzt Textausrichtung zurueck

    def mouseText(self,nachricht,x_pos,y_pos,x_pos_offset,l,b,r1,g1,b1): #funktion die text ueber dem Cursor erstellt
        fill(255,255,255)
        stroke(3)
        rect(x_pos-x_pos_offset,y_pos-20,l,b)
        fill(r1,g1,b1)
        text(nachricht,x_pos-x_pos_offset+10,y_pos+10)
        
    def ladeSchriftart(self,fontName, xsize): #lead eine Schritart
        self.font = loadFont(fontName) #bestimmt die Schriftart des Games
        textFont(self.font,xsize)

        
        
    
