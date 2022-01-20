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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 404)
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
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lnedit_playerName = QLineEdit(self.frame_2)
        self.lnedit_playerName.setObjectName(u"lnedit_playerName")
        sizePolicy.setHeightForWidth(self.lnedit_playerName.sizePolicy().hasHeightForWidth())
        self.lnedit_playerName.setSizePolicy(sizePolicy)
        self.lnedit_playerName.setMinimumSize(QSize(0, 50))
        self.lnedit_playerName.setMaximumSize(QSize(16777215, 60))
        self.lnedit_playerName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lnedit_playerName)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lnedit_icon = QLineEdit(self.frame_3)
        self.lnedit_icon.setObjectName(u"lnedit_icon")
        sizePolicy.setHeightForWidth(self.lnedit_icon.sizePolicy().hasHeightForWidth())
        self.lnedit_icon.setSizePolicy(sizePolicy)
        self.lnedit_icon.setMinimumSize(QSize(0, 50))
        self.lnedit_icon.setMaximumSize(QSize(16777215, 60))
        self.lnedit_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lnedit_icon)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.lnedit_budget = QLineEdit(self.frame)
        self.lnedit_budget.setObjectName(u"lnedit_budget")
        sizePolicy.setHeightForWidth(self.lnedit_budget.sizePolicy().hasHeightForWidth())
        self.lnedit_budget.setSizePolicy(sizePolicy)
        self.lnedit_budget.setMinimumSize(QSize(0, 50))
        self.lnedit_budget.setMaximumSize(QSize(16777215, 60))
        self.lnedit_budget.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lnedit_budget)


        self.verticalLayout.addWidget(self.frame)

        self.wdg_buttonContainer = QWidget(self.centralwidget)
        self.wdg_buttonContainer.setObjectName(u"wdg_buttonContainer")
        self.wdg_buttonContainer.setMinimumSize(QSize(0, 50))
        self.wdg_buttonContainer.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.wdg_buttonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_exitNewPlayer = QPushButton(self.wdg_buttonContainer)
        self.btn_exitNewPlayer.setObjectName(u"btn_exitNewPlayer")
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
        self.label_3.setText(QCoreApplication.translate("Form", u"Player Name", None))
        self.lnedit_playerName.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.lnedit_icon.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Guthaben:", None))
        self.lnedit_budget.setText("")
        self.btn_exitNewPlayer.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.btn_commitNewPlayer.setText(QCoreApplication.translate("Form", u"COMMIT", None))
    # retranslateUi

