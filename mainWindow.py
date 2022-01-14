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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(908, 857)
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
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.btn_Create_Player_1 = QPushButton(self.centralwidget)
        self.btn_Create_Player_1.setObjectName(u"btn_Create_Player_1")

        self.verticalLayout_3.addWidget(self.btn_Create_Player_1)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.bt_Create_Player_2 = QPushButton(self.centralwidget)
        self.bt_Create_Player_2.setObjectName(u"bt_Create_Player_2")

        self.verticalLayout.addWidget(self.bt_Create_Player_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_Create_Player_1.released.connect(MainWindow.create_new_player)
        self.bt_Create_Player_2.pressed.connect(MainWindow.create_new_player)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zeichen: ", None))
        self.btn_Create_Player_1.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TicTacToe", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Guthaben: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zeichen: ", None))
        self.bt_Create_Player_2.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
    # retranslateUi

