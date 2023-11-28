# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(316, 300)
        self.buttonBox = QDialogButtonBox(Welcome)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(220, 220, 81, 51))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox_7 = QGroupBox(Welcome)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 10, 191, 71))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QSize(90, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.editProtokollant_2 = QLineEdit(self.groupBox_7)
        self.editProtokollant_2.setObjectName(u"editProtokollant_2")
        sizePolicy.setHeightForWidth(self.editProtokollant_2.sizePolicy().hasHeightForWidth())
        self.editProtokollant_2.setSizePolicy(sizePolicy)
        self.editProtokollant_2.setMinimumSize(QSize(10, 0))
        self.editProtokollant_2.setMaximumSize(QSize(16777215, 31))
        self.editProtokollant_2.setBaseSize(QSize(30, 0))
        font = QFont()
        font.setFamilies([u"Abyssinica SIL"])
        font.setPointSize(14)
        self.editProtokollant_2.setFont(font)
        self.editProtokollant_2.setMaxLength(100)

        self.verticalLayout_2.addWidget(self.editProtokollant_2)

        self.listWidget = QListWidget(Welcome)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 90, 191, 192))
        self.findDb = QPushButton(Welcome)
        self.findDb.setObjectName(u"findDb")
        self.findDb.setGeometry(QRect(220, 100, 81, 23))
        self.createDb = QPushButton(Welcome)
        self.createDb.setObjectName(u"createDb")
        self.createDb.setGeometry(QRect(220, 130, 81, 23))

        self.retranslateUi(Welcome)
        self.buttonBox.accepted.connect(Welcome.accept)
        self.buttonBox.rejected.connect(Welcome.reject)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"Willkommen", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Welcome", u"Protokollant", None))
        self.findDb.setText(QCoreApplication.translate("Welcome", u"find db", None))
        self.createDb.setText(QCoreApplication.translate("Welcome", u"create db", None))
    # retranslateUi

