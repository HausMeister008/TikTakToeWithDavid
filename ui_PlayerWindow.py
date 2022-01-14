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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 450)
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
        font = QFont()
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Player_Name_Edit = QLineEdit(self.centralwidget)
        self.Player_Name_Edit.setObjectName(u"Player_Name_Edit")
        sizePolicy.setHeightForWidth(self.Player_Name_Edit.sizePolicy().hasHeightForWidth())
        self.Player_Name_Edit.setSizePolicy(sizePolicy)
        self.Player_Name_Edit.setMinimumSize(QSize(0, 50))
        self.Player_Name_Edit.setMaximumSize(QSize(16777215, 60))
        self.Player_Name_Edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Player_Name_Edit)

        self.Icon_edit = QLineEdit(self.centralwidget)
        self.Icon_edit.setObjectName(u"Icon_edit")
        sizePolicy.setHeightForWidth(self.Icon_edit.sizePolicy().hasHeightForWidth())
        self.Icon_edit.setSizePolicy(sizePolicy)
        self.Icon_edit.setMinimumSize(QSize(0, 50))
        self.Icon_edit.setMaximumSize(QSize(16777215, 60))
        self.Icon_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Icon_edit)

        self.Budget_edit = QLineEdit(self.centralwidget)
        self.Budget_edit.setObjectName(u"Budget_edit")
        sizePolicy.setHeightForWidth(self.Budget_edit.sizePolicy().hasHeightForWidth())
        self.Budget_edit.setSizePolicy(sizePolicy)
        self.Budget_edit.setMinimumSize(QSize(0, 50))
        self.Budget_edit.setMaximumSize(QSize(16777215, 60))
        self.Budget_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Budget_edit)

        self.wdg_buttonContainer = QWidget(self.centralwidget)
        self.wdg_buttonContainer.setObjectName(u"wdg_buttonContainer")
        self.wdg_buttonContainer.setMinimumSize(QSize(0, 50))
        self.wdg_buttonContainer.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.wdg_buttonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.wdg_buttonContainer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.wdg_buttonContainer)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.wdg_buttonContainer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("Form", u"Quit", None))
        self.Player_Name_Edit.setText(QCoreApplication.translate("Form", u"Player Name", None))
        self.Icon_edit.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.Budget_edit.setText(QCoreApplication.translate("Form", u"Budget", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"COMMIT", None))
    # retranslateUi

