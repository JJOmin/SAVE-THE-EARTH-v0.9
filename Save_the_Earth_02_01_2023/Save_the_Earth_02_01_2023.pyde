"""
Projektname: Save The Earth Early Access 1.0
Authoren: Enis Inep & Leonhard Tilly
Datum: 02.01.2023 11.38 Uhr
Nahezu fertig, bsi beschriftung fehlt noch!!!
"""

from ReaderClass import*       #Import der Classe
from ControllerClass import*
from ViewClass import*
from SammlungClass import*
from ModelClass import*
from GameFinaleClass import*

controller = controllerClass() #Instanz der controllerClass
view = viewClass()             #Instanz der viewClass
sammlung = sammlungClass()     #Instanz der sammlungClass
finale = gameFinaleClass()     #Instanz der gameFinaleClass

def setup():
    size(1920,1080)           #bestimmt Fenstergroesse
    controller.laden()        #laed PictureList aus CSV & die verwendete Schriftart
    controller.tryUndExcept() #der funktionsaufruf ist eine Vererbung aus sammlungClass

def draw():
    controller.buttonBackground()    #controller der die Hintergrundfarbe der Buttons im Startmenue controlliert
    controller.hintergrundBilder()   #controller der fast alle hintergrundbilder des games (nur nicht waerend des gameFinales) laed
    controller.textAnimation()       #controller die Hintergrundbilder waerend des Prologes
    controller.animationDuration()   #controller fuer die funktion die eine "Animation" realisiert, die durch Verzoegerung nacheinander Bilder abspielt (Ladeanimation)
    controller.indivBilder()         #controller zum laden von Individuellen Bildern im verlauf des Spiels (z.B. Sprechblase oder )
    controller.overlay()             #controller zur darstellung der Overley Buttons (z.B. "Spiel Speichern","Menue", "Inventar Oeffnen") oder darstellung des Offenen Inventars
    controller.inHandBilder()        #controller zur darstellung der Items wenn sie ausgewaehlt sind
    controller.moonAnimation()       #controller zur Moonanimation
    controller.reactionNPC()         #controller zum erstellen von Reaktionen der NPCs auf Interaktion
    controller.gameFinaleAnimation() #controller des Epiloges des Games
    controller.inHandBilder()        #controller zum 2. mal um die Items in der Hand etwas fluessigere darzustellen
    controller.menueZeit()           #controller zum anzeigen der Zeit im Startmenue

def mouseClicked():
    controller.startMenueButtons()  #controller fuer die Buttons im startmenue (Klickabfrage)
    controller.interaktionText()    #controller fuer die Buttons im Prolog (Interaktionen mit der Maus)
    controller.interaktionRaum()    #controller fuer die Raum weiter/zurueck Buttons
    controller.overlayInteraktion() #Controller fuer die Interaktion der Maus mit dem Overlay (Speichern, Zuruekc zum Menue, Inventar...)
    controller.gibMirItemAbfrage()  #Controller fuer die Interaktion mit Prof/Ratte, sowie den Tueren & dem Teilehcenbeschleuniger
    controller.kuelschrankoeffnen() #Controller fuer die Interaktion mit dem Kuelschrank (nicht in gibMir, da sonst Buggs entstanden sind)
        
def keyPressed():
    controller.tastaturInteraktion() #controller fuer die Interaktion von Tastatur mit Game im Gesamte Spiel (RaumWeiter/zuruck, Interaktion mit Teilchenbeschleuniger...)
