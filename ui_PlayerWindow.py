# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_player_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 350)
        Form.setMinimumSize(QSize(350, 350))
        font = QFont()
        Form.setFont(font)
        Form.setStyleSheet(u"")
        self.actionQuit = QAction(Form)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.lb_Player_Number = QLabel(self.centralwidget)
        self.lb_Player_Number.setObjectName(u"lb_Player_Number")
        self.lb_Player_Number.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player_Number)

        self.lnedit_playerName = QLineEdit(self.centralwidget)
        self.lnedit_playerName.setObjectName(u"lnedit_playerName")
        sizePolicy.setHeightForWidth(self.lnedit_playerName.sizePolicy().hasHeightForWidth())
        self.lnedit_playerName.setSizePolicy(sizePolicy)
        self.lnedit_playerName.setMinimumSize(QSize(0, 50))
        self.lnedit_playerName.setMaximumSize(QSize(16777215, 60))
        self.lnedit_playerName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lnedit_playerName)

        self.lnedit_icon = QLineEdit(self.centralwidget)
        self.lnedit_icon.setObjectName(u"lnedit_icon")
        sizePolicy.setHeightForWidth(self.lnedit_icon.sizePolicy().hasHeightForWidth())
        self.lnedit_icon.setSizePolicy(sizePolicy)
        self.lnedit_icon.setMinimumSize(QSize(0, 50))
        self.lnedit_icon.setMaximumSize(QSize(16777215, 60))
        self.lnedit_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lnedit_icon)

        self.lnedit_budget = QLineEdit(self.centralwidget)
        self.lnedit_budget.setObjectName(u"lnedit_budget")
        sizePolicy.setHeightForWidth(self.lnedit_budget.sizePolicy().hasHeightForWidth())
        self.lnedit_budget.setSizePolicy(sizePolicy)
        self.lnedit_budget.setMinimumSize(QSize(0, 50))
        self.lnedit_budget.setMaximumSize(QSize(16777215, 60))
        self.lnedit_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lnedit_budget)

        self.wdg_buttonContainer = QWidget(self.centralwidget)
        self.wdg_buttonContainer.setObjectName(u"wdg_buttonContainer")
        self.wdg_buttonContainer.setMinimumSize(QSize(0, 50))
        self.wdg_buttonContainer.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.wdg_buttonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_exitNewPlayer = QPushButton(self.wdg_buttonContainer)
        self.btn_exitNewPlayer.setObjectName(u"btn_exitNewPlayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_exitNewPlayer.sizePolicy().hasHeightForWidth())
        self.btn_exitNewPlayer.setSizePolicy(sizePolicy1)
        self.btn_exitNewPlayer.setMinimumSize(QSize(0, 50))
        self.btn_exitNewPlayer.setMaximumSize(QSize(16777215, 60))
        self.btn_exitNewPlayer.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_exitNewPlayer)

        self.btn_commitNewPlayer = QPushButton(self.wdg_buttonContainer)
        self.btn_commitNewPlayer.setObjectName(u"btn_commitNewPlayer")
        sizePolicy1.setHeightForWidth(self.btn_commitNewPlayer.sizePolicy().hasHeightForWidth())
        self.btn_commitNewPlayer.setSizePolicy(sizePolicy1)
        self.btn_commitNewPlayer.setMinimumSize(QSize(0, 50))
        self.btn_commitNewPlayer.setMaximumSize(QSize(16777215, 60))
        self.btn_commitNewPlayer.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_commitNewPlayer)


        self.verticalLayout.addWidget(self.wdg_buttonContainer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        self.btn_exitNewPlayer.clicked.connect(Form.exit_new_player)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("Form", u"Quit", None))
        self.lb_Player_Number.setText(QCoreApplication.translate("Form", u"Player 1", None))
        self.lnedit_playerName.setText(QCoreApplication.translate("Form", u"Player Name", None))
        self.lnedit_icon.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.lnedit_budget.setText(QCoreApplication.translate("Form", u"Guthaben:", None))
        self.btn_exitNewPlayer.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.btn_commitNewPlayer.setText(QCoreApplication.translate("Form", u"COMMIT", None))
    # retranslateUi

