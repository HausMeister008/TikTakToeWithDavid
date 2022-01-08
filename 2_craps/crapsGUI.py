import sys
# from PySide2.QtCore import (Qt)
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow)
from PySide2.QtGui import (QFont, QPaintEvent,QIntValidator, QPaintEvent)

from craps import *
from ui_craps import Ui_MainWindow
       
class CrapsWindow(QMainWindow, Ui_MainWindow):
    """2-Spieler GUI für das Wuerfelspiel Craps.

    Für Python/Pyside2/Qt umgesetzt nach einer Java/awt/swing Version von Thomas Schaller vom 19.06.2012.

    Version 12.2021
    Author S. Gebert
    """
    _spielleitung: Spielleitung
    
    def __init__(self):
        """Erstelle die Startumgebung."""
        super().__init__()
        # UI Komponenten anpassen
        self.setupUi(self)
        self.lineEdit_einsatz_spieler_1.setValidator( QIntValidator(0, 999, self) )
        self.lineEdit_einsatz_spieler_2.setValidator( QIntValidator(0, 999, self) )
        
        # Startumgebung erzeugen
        self._spielleitung = Spielleitung()
        self._spielleitung.add_spieler(Spieler(100)) #Startguthaben 100
        self._spielleitung.add_spieler(Spieler(100)) #Startguthaben 100
        self.label_meldung.setText(u"Bitte tätigen Sie Ihre Einsätze")
        self._update_display()
        
    def _update_display(self):
        """Aktualisiere die angezeigten Informationen."""
        sp1: Spieler = self._spielleitung.get_spieler(0)
        sp2: Spieler = self._spielleitung.get_spieler(1)
        self.lineEdit_guthaben_spieler_1.setText(str(sp1.guthaben))
        self.lineEdit_guthaben_spieler_2.setText(str(sp2.guthaben))
        if sp1.shooter:
            self.frame_spieler_1.setStyleSheet('background-color: lightgray;')
            self.frame_spieler_2.setStyleSheet('background-color: rgb(230,230,230);')
            self.label_spieler_1.setText("Spieler 1: Shooter")
            self.label_spieler_2.setText("Spieler 2: Fader")
        else:
            self.frame_spieler_1.setStyleSheet('background-color: rgb(230,230,230);')
            self.frame_spieler_2.setStyleSheet('background-color: lightgray;')
            self.label_spieler_1.setText("Spieler 1: Fader")
            self.label_spieler_2.setText("Spieler 2: Shooter")
        if (not self.lineEdit_einsatz_spieler_1.isEnabled() and
            not self.lineEdit_einsatz_spieler_2.isEnabled()):
            if sp1.shooter:
                self.label_meldung.setText("Spieler 1 muss würfeln")
            else:
                self.label_meldung.setText("Spieler 2 muss würfeln")            
        
        
    def bt_setzen_spieler1_clicked(self, checked:bool):
        """Aktion: Spieler 1 setzt Geld"""
        self._spielleitung.get_spieler(0).setze(int(self.lineEdit_einsatz_spieler_1.text()))
        self.lineEdit_einsatz_spieler_1.setEnabled(False)
        self.pushButton_setzen_spieler_1.setEnabled(False)
        self._update_display()

    def bt_setzen_spieler2_clicked(self, checked:bool):
        """Aktion: Spieler 2 setzt Geld"""
        self._spielleitung.get_spieler(1).setze(int(self.lineEdit_einsatz_spieler_2.text()))
        self.lineEdit_einsatz_spieler_2.setEnabled(False)
        self.pushButton_setzen_spieler_2.setEnabled(False)
        self._update_display()

    def wg_wuerfel_clicked(self):
        """Aktion: Würfeln"""
        if (not self.lineEdit_einsatz_spieler_1.isEnabled() and
            not self.lineEdit_einsatz_spieler_2.isEnabled()):
            self._spielleitung.get_wuerfel(0).wuerfeln()
            self._spielleitung.get_wuerfel(1).wuerfeln()
            self.diceWidget.setDiceNumber(1,self._spielleitung.get_wuerfel(0).wurf)
            self.diceWidget.setDiceNumber(2,self._spielleitung.get_wuerfel(1).wurf)
            
            if self._spielleitung.auswerten():
                # Einsatz wieder auf 0 setzen und Buttons zum Setzen aktivieren
                self.lineEdit_einsatz_spieler_1.setText("0")
                self.lineEdit_einsatz_spieler_1.setEnabled(True)
                self.pushButton_setzen_spieler_1.setEnabled(True)
                self.lineEdit_einsatz_spieler_2.setText("0")
                self.lineEdit_einsatz_spieler_2.setEnabled(True)
                self.pushButton_setzen_spieler_2.setEnabled(True)
                
                if self._spielleitung.gewinnwurf():
                    self.label_meldung.setText("Gewonnen! Bitte setzen Sie erneut!")
                else:
                    self.label_meldung.setText("Verloren! Bitte setzen Sie erneut!")
                self._spielleitung.neuesSpiel()
            self._update_display()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrapsWindow()
    window.show()
    app.exec_()
