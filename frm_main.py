# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Calibri"])
        self.centralwidget.setFont(font)
        self.lb_headline = QLabel(self.centralwidget)
        self.lb_headline.setObjectName(u"lb_headline")
        self.lb_headline.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_headline.setGeometry(QRect(300, 0, 600, 70))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setItalic(False)
        self.lb_headline.setFont(font1)
        self.lb_headline.setAlignment(Qt.AlignCenter)
        self.fr_player1 = QFrame(self.centralwidget)
        self.fr_player1.setObjectName(u"fr_player1")
        self.fr_player1.setGeometry(QRect(0, 0, 300, 900))
        self.fr_player1.setFrameShape(QFrame.StyledPanel)
        self.fr_player1.setFrameShadow(QFrame.Raised)
        self.lb_player_1_headline = QLabel(self.fr_player1)
        self.lb_player_1_headline.setObjectName(u"lb_player_1_headline")
        self.lb_player_1_headline.setGeometry(QRect(10, 0, 280, 71))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        self.lb_player_1_headline.setFont(font2)
        self.lb_player_1_headline.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_2 = QLabel(self.fr_player1)
        self.lb_player_1_headline_2.setObjectName(u"lb_player_1_headline_2")
        self.lb_player_1_headline_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_2.setGeometry(QRect(10, 70, 280, 71))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        self.lb_player_1_headline_2.setFont(font3)
        self.lb_player_1_headline_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_2.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_3 = QLabel(self.fr_player1)
        self.lb_player_1_headline_3.setObjectName(u"lb_player_1_headline_3")
        self.lb_player_1_headline_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_3.setGeometry(QRect(10, 140, 280, 71))
        self.lb_player_1_headline_3.setFont(font3)
        self.lb_player_1_headline_3.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_4 = QLabel(self.fr_player1)
        self.lb_player_1_headline_4.setObjectName(u"lb_player_1_headline_4")
        self.lb_player_1_headline_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_4.setGeometry(QRect(10, 210, 280, 71))
        self.lb_player_1_headline_4.setFont(font3)
        self.lb_player_1_headline_4.setAlignment(Qt.AlignCenter)
        self.fr_player2 = QFrame(self.centralwidget)
        self.fr_player2.setObjectName(u"fr_player2")
        self.fr_player2.setGeometry(QRect(900, 0, 300, 900))
        self.fr_player2.setFrameShape(QFrame.StyledPanel)
        self.fr_player2.setFrameShadow(QFrame.Raised)
        self.lb_player_2_headline = QLabel(self.fr_player2)
        self.lb_player_2_headline.setObjectName(u"lb_player_2_headline")
        self.lb_player_2_headline.setGeometry(QRect(10, 0, 280, 71))
        self.lb_player_2_headline.setFont(font1)
        self.lb_player_2_headline.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_7 = QLabel(self.fr_player2)
        self.lb_player_1_headline_7.setObjectName(u"lb_player_1_headline_7")
        self.lb_player_1_headline_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_7.setGeometry(QRect(10, 70, 280, 71))
        self.lb_player_1_headline_7.setFont(font3)
        self.lb_player_1_headline_7.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_6 = QLabel(self.fr_player2)
        self.lb_player_1_headline_6.setObjectName(u"lb_player_1_headline_6")
        self.lb_player_1_headline_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_6.setGeometry(QRect(10, 210, 280, 71))
        self.lb_player_1_headline_6.setFont(font3)
        self.lb_player_1_headline_6.setAlignment(Qt.AlignCenter)
        self.lb_player_1_headline_5 = QLabel(self.fr_player2)
        self.lb_player_1_headline_5.setObjectName(u"lb_player_1_headline_5")
        self.lb_player_1_headline_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_player_1_headline_5.setGeometry(QRect(10, 140, 280, 71))
        self.lb_player_1_headline_5.setFont(font3)
        self.lb_player_1_headline_5.setAlignment(Qt.AlignCenter)
        self.fr_Gameboard = QFrame(self.centralwidget)
        self.fr_Gameboard.setObjectName(u"fr_Gameboard")
        self.fr_Gameboard.setGeometry(QRect(300, 70, 600, 830))
        self.fr_Gameboard.setFrameShape(QFrame.StyledPanel)
        self.fr_Gameboard.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lb_headline.setText(QCoreApplication.translate("MainWindow", u"TicTacToe", None))
        self.lb_player_1_headline.setText(QCoreApplication.translate("MainWindow", u"Player1", None))
        self.lb_player_1_headline_2.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lb_player_1_headline_3.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
        self.lb_player_1_headline_4.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.lb_player_2_headline.setText(QCoreApplication.translate("MainWindow", u"Player2", None))
        self.lb_player_1_headline_7.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lb_player_1_headline_6.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.lb_player_1_headline_5.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
    # retranslateUi

