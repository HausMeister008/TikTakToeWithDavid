# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_field_size.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(447, 459)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.sl_field_size = QSlider(Dialog)
        self.sl_field_size.setObjectName(u"sl_field_size")
        self.sl_field_size.setMaximum(21)
        self.sl_field_size.setPageStep(3)
        self.sl_field_size.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sl_field_size)

        self.lb_current_field_size = QLabel(Dialog)
        self.lb_current_field_size.setObjectName(u"lb_current_field_size")

        self.verticalLayout.addWidget(self.lb_current_field_size)

        self.Commit_fiel_size = QPushButton(Dialog)
        self.Commit_fiel_size.setObjectName(u"Commit_fiel_size")

        self.verticalLayout.addWidget(self.Commit_fiel_size)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.sl_field_size.valueChanged.connect(self.lb_current_field_size.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Wich size should the field be ?", None))
        self.lb_current_field_size.setText(QCoreApplication.translate("Dialog", u"Current selected Fieldsize", None))
        self.Commit_fiel_size.setText(QCoreApplication.translate("Dialog", u"Commit", None))
    # retranslateUi

