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
        MainWindow.resize(1232, 992)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        sizePolicy.setHeightForWidth(self.fr_player1.sizePolicy().hasHeightForWidth())
        self.fr_player1.setSizePolicy(sizePolicy)
        self.fr_player1.setMinimumSize(QSize(200, 500))
        self.fr_player1.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.fr_player1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.lb_Player_1_headline = QLabel(self.fr_player1)
        self.lb_Player_1_headline.setObjectName(u"lb_Player_1_headline")
        self.lb_Player_1_headline.setMinimumSize(QSize(0, 40))
        self.lb_Player_1_headline.setMaximumSize(QSize(16777215, 60))
        self.lb_Player_1_headline.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Player_1_headline)

        self.lb_Player1_name = QLabel(self.fr_player1)
        self.lb_Player1_name.setObjectName(u"lb_Player1_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_Player1_name.sizePolicy().hasHeightForWidth())
        self.lb_Player1_name.setSizePolicy(sizePolicy1)
        self.lb_Player1_name.setMinimumSize(QSize(0, 40))
        self.lb_Player1_name.setMaximumSize(QSize(16777215, 60))
        self.lb_Player1_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Player1_name)

        self.lb_Player1_budget = QLabel(self.fr_player1)
        self.lb_Player1_budget.setObjectName(u"lb_Player1_budget")
        sizePolicy1.setHeightForWidth(self.lb_Player1_budget.sizePolicy().hasHeightForWidth())
        self.lb_Player1_budget.setSizePolicy(sizePolicy1)
        self.lb_Player1_budget.setMinimumSize(QSize(0, 40))
        self.lb_Player1_budget.setMaximumSize(QSize(16777215, 60))
        self.lb_Player1_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Player1_budget)

        self.lb_Player1_bet_value = QLabel(self.fr_player1)
        self.lb_Player1_bet_value.setObjectName(u"lb_Player1_bet_value")
        sizePolicy1.setHeightForWidth(self.lb_Player1_bet_value.sizePolicy().hasHeightForWidth())
        self.lb_Player1_bet_value.setSizePolicy(sizePolicy1)
        self.lb_Player1_bet_value.setMinimumSize(QSize(0, 40))
        self.lb_Player1_bet_value.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.lb_Player1_bet_value.setFont(font1)
        self.lb_Player1_bet_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Player1_bet_value)

        self.sl_player1 = QSlider(self.fr_player1)
        self.sl_player1.setObjectName(u"sl_player1")
        self.sl_player1.setMinimumSize(QSize(0, 50))
        self.sl_player1.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sl_player1)

        self.lp_player1_sl_value = QLabel(self.fr_player1)
        self.lp_player1_sl_value.setObjectName(u"lp_player1_sl_value")
        sizePolicy1.setHeightForWidth(self.lp_player1_sl_value.sizePolicy().hasHeightForWidth())
        self.lp_player1_sl_value.setSizePolicy(sizePolicy1)
        self.lp_player1_sl_value.setMinimumSize(QSize(0, 40))
        self.lp_player1_sl_value.setMaximumSize(QSize(16777215, 60))
        self.lp_player1_sl_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lp_player1_sl_value)

        self.lb_Player1_icon = QLabel(self.fr_player1)
        self.lb_Player1_icon.setObjectName(u"lb_Player1_icon")
        sizePolicy.setHeightForWidth(self.lb_Player1_icon.sizePolicy().hasHeightForWidth())
        self.lb_Player1_icon.setSizePolicy(sizePolicy)
        self.lb_Player1_icon.setMinimumSize(QSize(0, 40))
        self.lb_Player1_icon.setMaximumSize(QSize(16777215, 60))
        self.lb_Player1_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Player1_icon)

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

        self.fr_game_board = QFrame(self.fr_mainContent)
        self.fr_game_board.setObjectName(u"fr_game_board")
        sizePolicy.setHeightForWidth(self.fr_game_board.sizePolicy().hasHeightForWidth())
        self.fr_game_board.setSizePolicy(sizePolicy)
        self.fr_game_board.setMinimumSize(QSize(400, 450))
        self.fr_game_board.setFrameShape(QFrame.StyledPanel)
        self.fr_game_board.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.fr_game_board)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_3.addWidget(self.fr_game_board)

        self.lb_outputField = QLabel(self.fr_mainContent)
        self.lb_outputField.setObjectName(u"lb_outputField")
        sizePolicy.setHeightForWidth(self.lb_outputField.sizePolicy().hasHeightForWidth())
        self.lb_outputField.setSizePolicy(sizePolicy)
        self.lb_outputField.setMinimumSize(QSize(0, 40))
        self.lb_outputField.setMaximumSize(QSize(16777215, 60))
        self.lb_outputField.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_outputField)

        self.btn_qss_toggle = QPushButton(self.fr_mainContent)
        self.btn_qss_toggle.setObjectName(u"btn_qss_toggle")

        self.verticalLayout_3.addWidget(self.btn_qss_toggle)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sl_field_size = QSlider(self.fr_mainContent)
        self.sl_field_size.setObjectName(u"sl_field_size")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sl_field_size.sizePolicy().hasHeightForWidth())
        self.sl_field_size.setSizePolicy(sizePolicy3)
        self.sl_field_size.setMinimumSize(QSize(0, 20))
        self.sl_field_size.setMaximumSize(QSize(16777215, 75))
        self.sl_field_size.setMaximum(13)
        self.sl_field_size.setSingleStep(1)
        self.sl_field_size.setPageStep(1)
        self.sl_field_size.setValue(1)
        self.sl_field_size.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sl_field_size)

        self.btn_render = QPushButton(self.fr_mainContent)
        self.btn_render.setObjectName(u"btn_render")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_render.sizePolicy().hasHeightForWidth())
        self.btn_render.setSizePolicy(sizePolicy4)
        self.btn_render.setMinimumSize(QSize(0, 75))
        self.btn_render.setMaximumSize(QSize(16777215, 75))

        self.horizontalLayout_2.addWidget(self.btn_render)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.fr_mainContent)

        self.fr_player2 = QFrame(self.centralwidget)
        self.fr_player2.setObjectName(u"fr_player2")
        sizePolicy.setHeightForWidth(self.fr_player2.sizePolicy().hasHeightForWidth())
        self.fr_player2.setSizePolicy(sizePolicy)
        self.fr_player2.setMinimumSize(QSize(200, 500))
        self.fr_player2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.fr_player2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.lb_Player_2_headline = QLabel(self.fr_player2)
        self.lb_Player_2_headline.setObjectName(u"lb_Player_2_headline")
        self.lb_Player_2_headline.setMinimumSize(QSize(0, 40))
        self.lb_Player_2_headline.setMaximumSize(QSize(16777215, 60))
        self.lb_Player_2_headline.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player_2_headline)

        self.lb_Player2_name = QLabel(self.fr_player2)
        self.lb_Player2_name.setObjectName(u"lb_Player2_name")
        sizePolicy.setHeightForWidth(self.lb_Player2_name.sizePolicy().hasHeightForWidth())
        self.lb_Player2_name.setSizePolicy(sizePolicy)
        self.lb_Player2_name.setMinimumSize(QSize(0, 40))
        self.lb_Player2_name.setMaximumSize(QSize(16777215, 60))
        self.lb_Player2_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player2_name)

        self.lb_Player2_budget = QLabel(self.fr_player2)
        self.lb_Player2_budget.setObjectName(u"lb_Player2_budget")
        sizePolicy.setHeightForWidth(self.lb_Player2_budget.sizePolicy().hasHeightForWidth())
        self.lb_Player2_budget.setSizePolicy(sizePolicy)
        self.lb_Player2_budget.setMinimumSize(QSize(0, 40))
        self.lb_Player2_budget.setMaximumSize(QSize(16777215, 60))
        self.lb_Player2_budget.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player2_budget)

        self.lb_Player2_bet_value = QLabel(self.fr_player2)
        self.lb_Player2_bet_value.setObjectName(u"lb_Player2_bet_value")
        sizePolicy.setHeightForWidth(self.lb_Player2_bet_value.sizePolicy().hasHeightForWidth())
        self.lb_Player2_bet_value.setSizePolicy(sizePolicy)
        self.lb_Player2_bet_value.setMinimumSize(QSize(0, 40))
        self.lb_Player2_bet_value.setMaximumSize(QSize(16777215, 60))
        self.lb_Player2_bet_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player2_bet_value)

        self.sl_player2 = QSlider(self.fr_player2)
        self.sl_player2.setObjectName(u"sl_player2")
        self.sl_player2.setMinimumSize(QSize(0, 50))
        self.sl_player2.setValue(0)
        self.sl_player2.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sl_player2)

        self.lp_player2_sl_value = QLabel(self.fr_player2)
        self.lp_player2_sl_value.setObjectName(u"lp_player2_sl_value")
        sizePolicy1.setHeightForWidth(self.lp_player2_sl_value.sizePolicy().hasHeightForWidth())
        self.lp_player2_sl_value.setSizePolicy(sizePolicy1)
        self.lp_player2_sl_value.setMinimumSize(QSize(0, 40))
        self.lp_player2_sl_value.setMaximumSize(QSize(16777215, 60))
        self.lp_player2_sl_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lp_player2_sl_value)

        self.lb_Player2_icon = QLabel(self.fr_player2)
        self.lb_Player2_icon.setObjectName(u"lb_Player2_icon")
        sizePolicy.setHeightForWidth(self.lb_Player2_icon.sizePolicy().hasHeightForWidth())
        self.lb_Player2_icon.setSizePolicy(sizePolicy)
        self.lb_Player2_icon.setMinimumSize(QSize(0, 40))
        self.lb_Player2_icon.setMaximumSize(QSize(16777215, 60))
        self.lb_Player2_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_Player2_icon)

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
        QWidget.setTabOrder(self.sl_player1, self.sl_player2)
        QWidget.setTabOrder(self.sl_player2, self.btn_Create_Player_1)
        QWidget.setTabOrder(self.btn_Create_Player_1, self.btn_Create_Player_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lb_Player_1_headline.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.lb_Player1_name.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lb_Player1_budget.setText(QCoreApplication.translate("MainWindow", u"Budget:", None))
        self.lb_Player1_bet_value.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.lp_player1_sl_value.setText("")
        self.lb_Player1_icon.setText(QCoreApplication.translate("MainWindow", u"Icon:", None))
        self.btn_Create_Player_1.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
        self.lb_mainHeadline.setText(QCoreApplication.translate("MainWindow", u"TicTacToe", None))
        self.lb_outputField.setText("")
        self.btn_qss_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle Mode", None))
        self.btn_render.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.lb_Player_2_headline.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.lb_Player2_name.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.lb_Player2_budget.setText(QCoreApplication.translate("MainWindow", u"Budget:", None))
        self.lb_Player2_bet_value.setText(QCoreApplication.translate("MainWindow", u"Einsatz: ", None))
        self.lp_player2_sl_value.setText("")
        self.lb_Player2_icon.setText(QCoreApplication.translate("MainWindow", u"Icon:", None))
        self.btn_Create_Player_2.setText(QCoreApplication.translate("MainWindow", u"Create Player", None))
    # retranslateUi

