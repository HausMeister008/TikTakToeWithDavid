# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crapsaiRGLH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DiceWidget import DiceWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 213)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_spieler_1 = QFrame(self.centralwidget)
        self.frame_spieler_1.setObjectName(u"frame_spieler_1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_spieler_1.sizePolicy().hasHeightForWidth())
        self.frame_spieler_1.setSizePolicy(sizePolicy)
        self.frame_spieler_1.setFrameShape(QFrame.StyledPanel)
        self.frame_spieler_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_spieler_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_spieler_1 = QLabel(self.frame_spieler_1)
        self.label_spieler_1.setObjectName(u"label_spieler_1")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_spieler_1.setFont(font)
        self.label_spieler_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_spieler_1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_guthaben_spieler_1 = QLabel(self.frame_spieler_1)
        self.label_guthaben_spieler_1.setObjectName(u"label_guthaben_spieler_1")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_guthaben_spieler_1)

        self.lineEdit_guthaben_spieler_1 = QLineEdit(self.frame_spieler_1)
        self.lineEdit_guthaben_spieler_1.setObjectName(u"lineEdit_guthaben_spieler_1")
        self.lineEdit_guthaben_spieler_1.setEnabled(True)
        self.lineEdit_guthaben_spieler_1.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_guthaben_spieler_1)

        self.label_einsatz_spieler_1 = QLabel(self.frame_spieler_1)
        self.label_einsatz_spieler_1.setObjectName(u"label_einsatz_spieler_1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_einsatz_spieler_1)

        self.lineEdit_einsatz_spieler_1 = QLineEdit(self.frame_spieler_1)
        self.lineEdit_einsatz_spieler_1.setObjectName(u"lineEdit_einsatz_spieler_1")
        self.lineEdit_einsatz_spieler_1.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_einsatz_spieler_1)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_setzen_spieler_1 = QPushButton(self.frame_spieler_1)
        self.pushButton_setzen_spieler_1.setObjectName(u"pushButton_setzen_spieler_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_setzen_spieler_1.sizePolicy().hasHeightForWidth())
        self.pushButton_setzen_spieler_1.setSizePolicy(sizePolicy1)
        self.pushButton_setzen_spieler_1.setMaximumSize(QSize(80, 27))

        self.horizontalLayout.addWidget(self.pushButton_setzen_spieler_1)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addWidget(self.frame_spieler_1)

        self.widget_spielfeld = QWidget(self.centralwidget)
        self.widget_spielfeld.setObjectName(u"widget_spielfeld")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_spielfeld.sizePolicy().hasHeightForWidth())
        self.widget_spielfeld.setSizePolicy(sizePolicy2)
        self.spielfeldLayout = QVBoxLayout(self.widget_spielfeld)
        self.spielfeldLayout.setObjectName(u"spielfeldLayout")
        self.diceWidget = DiceWidget(self.widget_spielfeld)
        self.diceWidget.setObjectName(u"diceWidget")
        sizePolicy2.setHeightForWidth(self.diceWidget.sizePolicy().hasHeightForWidth())
        self.diceWidget.setSizePolicy(sizePolicy2)

        self.spielfeldLayout.addWidget(self.diceWidget)

        self.label_meldung = QLabel(self.widget_spielfeld)
        self.label_meldung.setObjectName(u"label_meldung")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_meldung.sizePolicy().hasHeightForWidth())
        self.label_meldung.setSizePolicy(sizePolicy3)
        self.label_meldung.setMinimumSize(QSize(200, 40))
        self.label_meldung.setTextFormat(Qt.AutoText)
        self.label_meldung.setAlignment(Qt.AlignCenter)

        self.spielfeldLayout.addWidget(self.label_meldung)


        self.horizontalLayout_4.addWidget(self.widget_spielfeld)

        self.frame_spieler_2 = QFrame(self.centralwidget)
        self.frame_spieler_2.setObjectName(u"frame_spieler_2")
        sizePolicy.setHeightForWidth(self.frame_spieler_2.sizePolicy().hasHeightForWidth())
        self.frame_spieler_2.setSizePolicy(sizePolicy)
        self.frame_spieler_2.setFrameShape(QFrame.StyledPanel)
        self.frame_spieler_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_spieler_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_spieler_2 = QLabel(self.frame_spieler_2)
        self.label_spieler_2.setObjectName(u"label_spieler_2")
        self.label_spieler_2.setFont(font)
        self.label_spieler_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_spieler_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_guthaben_spieler_2 = QLabel(self.frame_spieler_2)
        self.label_guthaben_spieler_2.setObjectName(u"label_guthaben_spieler_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_guthaben_spieler_2)

        self.lineEdit_guthaben_spieler_2 = QLineEdit(self.frame_spieler_2)
        self.lineEdit_guthaben_spieler_2.setObjectName(u"lineEdit_guthaben_spieler_2")
        self.lineEdit_guthaben_spieler_2.setEnabled(True)
        self.lineEdit_guthaben_spieler_2.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_guthaben_spieler_2)

        self.label_einsatz_spieler_2 = QLabel(self.frame_spieler_2)
        self.label_einsatz_spieler_2.setObjectName(u"label_einsatz_spieler_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_einsatz_spieler_2)

        self.lineEdit_einsatz_spieler_2 = QLineEdit(self.frame_spieler_2)
        self.lineEdit_einsatz_spieler_2.setObjectName(u"lineEdit_einsatz_spieler_2")
        self.lineEdit_einsatz_spieler_2.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_einsatz_spieler_2)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_setzen_spieler_2 = QPushButton(self.frame_spieler_2)
        self.pushButton_setzen_spieler_2.setObjectName(u"pushButton_setzen_spieler_2")
        sizePolicy1.setHeightForWidth(self.pushButton_setzen_spieler_2.sizePolicy().hasHeightForWidth())
        self.pushButton_setzen_spieler_2.setSizePolicy(sizePolicy1)
        self.pushButton_setzen_spieler_2.setMaximumSize(QSize(80, 27))

        self.horizontalLayout_2.addWidget(self.pushButton_setzen_spieler_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addWidget(self.frame_spieler_2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_einsatz_spieler_1, self.lineEdit_einsatz_spieler_2)
        QWidget.setTabOrder(self.lineEdit_einsatz_spieler_2, self.pushButton_setzen_spieler_1)
        QWidget.setTabOrder(self.pushButton_setzen_spieler_1, self.pushButton_setzen_spieler_2)
        QWidget.setTabOrder(self.pushButton_setzen_spieler_2, self.lineEdit_guthaben_spieler_1)
        QWidget.setTabOrder(self.lineEdit_guthaben_spieler_1, self.lineEdit_guthaben_spieler_2)

        self.retranslateUi(MainWindow)
        self.pushButton_setzen_spieler_1.clicked.connect(MainWindow.bt_setzen_spieler1_clicked)
        self.pushButton_setzen_spieler_2.clicked.connect(MainWindow.bt_setzen_spieler2_clicked)
        self.diceWidget.clicked.connect(MainWindow.wg_wuerfel_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Craps Gui", None))
        self.label_spieler_1.setText(QCoreApplication.translate("MainWindow", u"Spieler 1", None))
        self.label_guthaben_spieler_1.setText(QCoreApplication.translate("MainWindow", u"Guthaben", None))
        self.label_einsatz_spieler_1.setText(QCoreApplication.translate("MainWindow", u"Einsatz", None))
        self.pushButton_setzen_spieler_1.setText(QCoreApplication.translate("MainWindow", u"setzen", None))
        self.label_meldung.setText(QCoreApplication.translate("MainWindow", u"Mein Craps-Spiel", None))
        self.label_spieler_2.setText(QCoreApplication.translate("MainWindow", u"Spieler 2", None))
        self.label_guthaben_spieler_2.setText(QCoreApplication.translate("MainWindow", u"Guthaben", None))
        self.label_einsatz_spieler_2.setText(QCoreApplication.translate("MainWindow", u"Einsatz", None))
        self.pushButton_setzen_spieler_2.setText(QCoreApplication.translate("MainWindow", u"setzen", None))
    # retranslateUi

