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
        Form.resize(694, 675)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Player_Name_Edit.sizePolicy().hasHeightForWidth())
        self.Player_Name_Edit.setSizePolicy(sizePolicy1)
        self.Player_Name_Edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Player_Name_Edit)

        self.Icon_edit = QLineEdit(self.centralwidget)
        self.Icon_edit.setObjectName(u"Icon_edit")
        sizePolicy1.setHeightForWidth(self.Icon_edit.sizePolicy().hasHeightForWidth())
        self.Icon_edit.setSizePolicy(sizePolicy1)
        self.Icon_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Icon_edit)

        self.Budget_edit = QLineEdit(self.centralwidget)
        self.Budget_edit.setObjectName(u"Budget_edit")
        sizePolicy1.setHeightForWidth(self.Budget_edit.sizePolicy().hasHeightForWidth())
        self.Budget_edit.setSizePolicy(sizePolicy1)
        self.Budget_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Budget_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Exit_add_player_window = QPushButton(self.centralwidget)
        self.Exit_add_player_window.setObjectName(u"Exit_add_player_window")
        sizePolicy.setHeightForWidth(self.Exit_add_player_window.sizePolicy().hasHeightForWidth())
        self.Exit_add_player_window.setSizePolicy(sizePolicy)
        self.Exit_add_player_window.setMaximumSize(QSize(400, 400))
        self.Exit_add_player_window.setFlat(True)

        self.horizontalLayout.addWidget(self.Exit_add_player_window)

        self.commit_add_player_window = QPushButton(self.centralwidget)
        self.commit_add_player_window.setObjectName(u"commit_add_player_window")
        sizePolicy.setHeightForWidth(self.commit_add_player_window.sizePolicy().hasHeightForWidth())
        self.commit_add_player_window.setSizePolicy(sizePolicy)
        self.commit_add_player_window.setMaximumSize(QSize(400, 400))
        self.commit_add_player_window.setFlat(True)

        self.horizontalLayout.addWidget(self.commit_add_player_window)


        self.verticalLayout.addLayout(self.horizontalLayout)


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
        self.Exit_add_player_window.setText(QCoreApplication.translate("Form", u"exit", None))
        self.commit_add_player_window.setText(QCoreApplication.translate("Form", u"commit", None))
    # retranslateUi

