from PySide2.QtCore import (Qt, QRect, QSize, Signal, QPoint)
from PySide2.QtWidgets import (QWidget)
from PySide2.QtWidgets import (QSizePolicy)
from PySide2.QtGui import (QPainter, QPixmap, QBrush, QColor,QPaintEvent)
    
class DiceWidget(QWidget):
    """A widget that displays two six sided dice.

    Version: 12.2021
    Author: S. Gebert
    """
    sprites: list[QPixmap]
    _number_dice: list[int]
    _dice_margin: int
    
    clicked = Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._background_color = QColor('white')
        self.sprites = [QPixmap("sprites/dice_"+str(i)+".gif") for i in range(1,7)]
        self._number_dice = [1,2]
        self._dice_margin = 10
                
    def paintEvent(self, e: QPaintEvent):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)
        painter.drawPixmap(QPoint(
            (rect.width() - self.sprites[self._number_dice[0]-1].width())/2 - (self.sprites[self._number_dice[0]-1].width()/2+self._dice_margin/2),
            (rect.height() - self.sprites[self._number_dice[0]-1].height())/2),
                           self.sprites[self._number_dice[0]-1])
        painter.drawPixmap(QPoint(
            (rect.width() - self.sprites[self._number_dice[1]-1].width())/2 + (self.sprites[self._number_dice[1]-1].width()/2+self._dice_margin/2),
            (rect.height() - self.sprites[self._number_dice[1]-1].height())/2),
                           self.sprites[self._number_dice[1]-1])
        painter.end()
    
    def mousePressEvent(self, e):
        self.clicked.emit()
    
    def setDiceNumber(self, dice: int, number: int) -> None:
        """set the given 'dice' to the given 'number'."""
        if not 1 <= dice <= len(self._number_dice):
            raise ValueError(f"Unknown dice: {dice}")
        if not 1 <= number <= 6:
            raise ValueError(f"number {number} not in range(1,7)")
        self._number_dice[dice-1] = number
        self.repaint()