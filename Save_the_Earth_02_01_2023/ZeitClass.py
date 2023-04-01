from datetime import datetime #importieren das datetime modul
class zeitClass():
    def __init__(self): #konstruktor
        self.__zeitJetzt = 0 #private Variable
        
    def zeitGeber(self): #getter
        return self.__zeitJetzt #return
    
    def zeitSetzer(self): #setter
        now = datetime.now() #zugriff auf datetime und wiedergabe der aktuellen zeit
        self.__zeitJetzt = now.strftime("%H:%M Uhr") #setzt neue Zeit ein (aus W3school gelernt)
        
        
