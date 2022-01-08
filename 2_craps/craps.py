"""Das Wuerfelspiel Craps.

Für Python umgesetzt nach einer Java Version von Thomas Schaller vom 19.06.2012.

Version 12.2021
Author S. Gebert
"""
import random

class Spieler:
    """Speichert die Daten eines Spielers für das Spiel Craps."""
    _guthaben: int
    _einsatz: int
    shooter: bool
    
    def __init__(self, guthaben: int):
        """Erzeuge einen Spieler mit einem bestimmten Startguthaben."""
        self._guthaben = guthaben
        self._einsatz = 0
        self.shooter = False
    
    @property
    def guthaben(self) -> int:
        """Das aktuelle Guthaben des Spielers"""
        return self._guthaben
    
    def setze(self, betrag: int):
        """Setze den Einsatz für das nächste Spiel"""
        self._einsatz += betrag
        self._guthaben -= betrag
        
    def gewonnen(self):
        """Rechne den Gewinn des Spielers ab, da er gewonnen hat."""
        self._guthaben += (2*self._einsatz)
        self._einsatz = 0
    
    def verloren(self):
        """Verliere den Einsatz, da der Spieler verloren hat."""
        self._einsatz = 0
        
class Wuerfel:
    _wurf: int
    def __init__(self):
        self.wuerfeln()
    @property  
    def wurf(self):
        """Augenzahl des letzten Wurfs."""
        return self._wurf
    def wuerfeln(self):
        """Würfel den Würfel."""
        self._wurf = random.randint(1,6)

class Spielleitung:
    """Spielleitung für das Würfelspiel Craps.

    Es werden die Mitspieler verwaltet, der aktuelle Spieler gespeichert,
    die Würfel erzeugt.
    Es können bis zu 6 Spieler am Spiel teilnehmen
    """
    spieler: list[Spieler]
    wuerfel0: Wuerfel
    wuerfel1: Wuerfel
    point: int
    
    def __init__(self):
        """Erzeuge die Spielleitung für Craps."""
        self.point = 0;
        self.wuerfel0 = Wuerfel()
        self.wuerfel1 = Wuerfel()
        self.spieler = list()
        
    def add_spieler(self, s: Spieler):
        """Melde einen Spieler bei der Spielleitung an."""
        self.spieler.append(s)
        if len(self.spieler) == 1:
            s.shooter = True
        else:
            s.shooter = False
    
    def gewinnwurf(self) -> bool:
        """Gib zurück, ob die aktuelle Würfelkombination ein Gewinnwurf ist."""
        augensumme = self.wuerfel0.wurf + self.wuerfel1.wurf
        return (
            # erster Wurf: Natural
            (self.point == 0 and (augensumme == 7 or augensumme == 11))
            or
            # weitere Würfe
            (self.point !=0 and augensumme == self.point) )

    
    def verlustwurf(self) -> bool:
        """Gib zurück, ob die aktuelle Würfelkombination ein Verlustwurf ist."""
        augensumme = self.wuerfel0.wurf + self.wuerfel1.wurf
        return (
            # erster Wurf: Crap
            (self.point == 0 and (augensumme == 2 or augensumme == 3 or augensumme == 12))
            or
            # weitere Würfe: 7 aus dem Spiel
            ( self.point != 0 and augensumme == 7 ) )
        
    def auswerten(self) -> bool:
        """Werte den letzten Würfelwurf aus.
    
        Falls es ein Gewinn- oder Verlustwurf ist,
        werden die Spieler über ihren Sieg/Verlust informiert
        """
        if self.gewinnwurf():
            # Alle Spieler haben verloren, nur Shooter hat gewonnen
            for s in self.spieler:
                if s.shooter:
                    s.gewonnen()
                else:
                    s.verloren()
            return True
        if self.verlustwurf():
            # Alle Spieler haben gewonnen, nur Shooter hat verloren
            for s in self.spieler:
                if s.shooter:
                    s.verloren()
                else:
                    s.gewonnen()
                pass
            return True
        # merke point beim ersten Wurf
        if self.point == 0:
            self.point = self.wuerfel0.wurf + self.wuerfel1.wurf
        return False
            
    def neuesSpiel(self):
        """Starte einen neuen Durchgang.

        Der Point wird zurückgesetzt und der nächste Spieler wird Shooter,
        falls der Shooter den vorherigen Durchgang verloren hat.
        """
        if self.verlustwurf():
            for s in self.spieler:
                if s.shooter:
                    s.shooter = False
                    # Der nächste Spieler (index+1) wird zu Shooter.
                    # Wenn der letzte Spieler shooter war muss es der erste werden,
                    # daher modulo Anzahl der Spieler
                    self.spieler[(self.spieler.index(s)+1) % len(self.spieler)].shooter = True
                    break
        self.point = 0
    
    def get_wuerfel(self, n: int) -> Wuerfel:
        """Gib den n-ten Würfel zurück."""
        if n == 0:
            return self.wuerfel0
        else:
            return self.wuerfel1
    def get_spieler(self, n: int) -> Spieler:
        """Gib den n-ten Spieler zurück."""
        return self.spieler[n]