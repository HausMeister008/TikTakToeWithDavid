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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 578)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fr_player1 = QFrame(self.centralwidget)
        self.fr_player1.setObjectName(u"fr_player1")
        self.fr_player1.setMinimumSize(QSize(200, 500))
        self.verticalLayout_2 = QVBoxLayout(self.fr_player1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.lb_player_1_headline = QLabel(self.fr_player1)
        self.lb_player_1_headline.setObjectName(u"lb_player_1_headline")
        self.lb_player_1_headline.setMinimumSize(QSize(0, 40))
        self.lb_player_1_headline.setMaximumSize(QSize(16777215, 60))
        self.lb_player_1_headline.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_player_1_headline)

        self.label_5 = QLabel(self.fr_player1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 60))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.fr_player1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777215, 60))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(self.fr_player1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalSlider = QSlider(self.fr_player1)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(self.fr_player1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setMaximumSize(QSize(16777215, 60))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.btn_Create_Player_1 = QPushButton(self.fr_player1)
        self.btn_Create_Player_1.setObjectName(u"btn_Create_Player_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_Create_Player_1.sizePolicy().hasHeightForWidth())
        self.btn_Create_Player_1.setSizePolicy(sizePolicy2)
        self.btn_Create_Player_1.setMinimumSize(QSize(0, 40))
        self.btn_Create_Player_1.setMaximumSize(QSize(16777215, 60))
        self.btn_Create_Player_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_Create_Player_1)


        self.horizontalLayout.addWidget(self.fr_player1)

        self.fr_mainContent = QFrame(self.centralwidget)
        self.fr_mainContent.setObjectName(u"fr_mainContent")
        self.fr_mainContent.setMinimumSize(QSize(0, 500))
        self.verticalLayout_3 = QVBoxLayout(self.fr_mainContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_mainHeadline = QLabel(self.fr_mainContent)
        self.lb_mainHeadline.setObjectName(u"lb_mainHeadline")
        sizePolicy.setHeightForWidth(self.lb_mainHeadline.sizePolicy().hasHeightForWidth())
        self.lb_mainHeadline.setSizePolicy(sizePolicy)
        self.lb_mainHeadline.setMinimumSize(QSize(0, 40))
        self.lb_mainHeadline.setMaximumSize(QSize(16777215, 16777215))
        self.lb_mainHeadline.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_mainHeadline, 0, Qt.AlignTop)

        self.frame = QFrame(self.fr_mainContent)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(400, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.btn_qss_reload = QPushButton(self.fr_mainContent)
        self.btn_qss_reload.setObjectName(u"btn_qss_reload")

        self.verticalLayout_3.addWidget(self.btn_qss_reload)

        self.btn_qss_reload_weird = QPushButton(self.fr_mainContent)
        self.btn_qss_reload_weird.setObjectName(u"btn_qss_reload_weird")

        self.verticalLayout_3.addWidget(self.btn_qss_reload_weird)

        self.lb_outputField = QLabel(self.fr_mainContent)
        self.lb_outputField.setObjectName(u"lb_outputField")
        sizePolicy.setHeightForWidth(self.lb_outputField.sizePolicy().hasHeightForWidth())
        self.lb_outputField.setSizePolicy(sizePolicy)
        self.lb_outputField.setMinimumSize(QSize(0, 40))
        self.lb_outputField.setMaximumSize(QSize(16777215, 60))
        self.lb_outputField.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_outputField)


        self.horizontalLayout.addWidget(self.fr_mainContent)

        self.fr_player2 = QFrame(self.centralwidget)
        self.fr_player2.setObjectName(u"fr_player2")
        self.fr_player2.setMinimumSize(QSize(200, 500))
        self.verticalLayout = QVBoxLayout(self.fr_player2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.lb_player_2_headline = QLabel(self.fr_player2)
        self.lb_player_2_headline.setObjectName(u"lb_player_2_headline")
        self.lb_player_2_headline.setMinimumSize(QSize(0, 40))
        self.lb_player_2_headline.setMaximumSize(QSize(16777215, 60))
        self.lb_player_2_headline.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_player_2_headline)

        self.label_9 = QLabel(self.fr_player2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(0, 40))
        self.label_9.setMaximumSize(QSize(16777215, 60))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_8 = QLabel(self.fr_player2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 60))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.fr_player2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 60))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalSlider_2 = QSlider(self.fr_player2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_2)

        self.label = QLabel(self.fr_player2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 60))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.btn_Create_Player_2 = QPushButton(self.fr_player2)
        self.btn_Create_Player_2.setObjectName(u"btn_Create_Player_2")
        sizePolicy.setHeightForWidth(self.btn_Create_Player_2.sizePolicy().hasHeightForWidth())
        self.btn_Create_Player_2.setSizePolicy(sizePolicy)
        self.btn_Create_Player_2.setMinimumSize(QSize(0, 40))
        self.btn_Create_Player_2.setMaximumSize(QSize(16777215, 60))
        self.btn_Create_Player_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_Create_Player_2)


        self.horizontalLayout.addWidget(self.fr_player2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_Create_Player_1.clicked.connect(MainWindow.create_new_player)
        self.btn_Create_Player_2.clicked.connect(MainWindow.create_new_player)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lb_player_1_headline.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zeichen: ", None))
        self.btn_Create_Player_1.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
        self.lb_mainHeadline.setText(QCoreApplication.translate("MainWindow", u"TicTacToe", None))
        self.btn_qss_reload.setText(QCoreApplication.translate("MainWindow", u"Reload, qss", None))
        self.btn_qss_reload_weird.setText(QCoreApplication.translate("MainWindow", u"Reload, weird", None))
        self.lb_outputField.setText("")
        self.lb_player_2_headline.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zeichen: ", None))
        self.btn_Create_Player_2.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
    # retranslateUi

