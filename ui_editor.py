# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editor.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QToolBar, QWidget)
import images_rc

class Ui_Editor(object):
    def setupUi(self, Editor):
        if not Editor.objectName():
            Editor.setObjectName(u"Editor")
        Editor.resize(623, 389)
        Editor.setMinimumSize(QSize(0, 0))
        Editor.setWindowTitle(u"Editor")
        icon = QIcon()
        icon.addFile(u":/images/images/table_edit.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/images/table_edit.png", QSize(), QIcon.Normal, QIcon.On)
        Editor.setWindowIcon(icon)
        self.action_xls = QAction(Editor)
        self.action_xls.setObjectName(u"action_xls")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/file_extension_xls.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_xls.setIcon(icon1)
        self.action_anwenden = QAction(Editor)
        self.action_anwenden.setObjectName(u"action_anwenden")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/accept.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_anwenden.setIcon(icon2)
        self.action_loeschen = QAction(Editor)
        self.action_loeschen.setObjectName(u"action_loeschen")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_loeschen.setIcon(icon3)
        self.action_zurueck = QAction(Editor)
        self.action_zurueck.setObjectName(u"action_zurueck")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/arrow_undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zurueck.setIcon(icon4)
        self.action_newline = QAction(Editor)
        self.action_newline.setObjectName(u"action_newline")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_newline.setIcon(icon5)
        self.actionAntworten_exportieren = QAction(Editor)
        self.actionAntworten_exportieren.setObjectName(u"actionAntworten_exportieren")
        self.actionAntworten_exportieren.setEnabled(False)
        self.action_Importieren = QAction(Editor)
        self.action_Importieren.setObjectName(u"action_Importieren")
        self.actionSqlQuery = QAction(Editor)
        self.actionSqlQuery.setObjectName(u"actionSqlQuery")
        self.actionSqlQuery.setCheckable(True)
        self.centralwidget = QWidget(Editor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setAutoScroll(False)
        self.tableView.setAutoScrollMargin(1)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tableView, 6, 0, 1, 1)

        self.queryTextEdit = QLineEdit(self.centralwidget)
        self.queryTextEdit.setObjectName(u"queryTextEdit")
        self.queryTextEdit.setMaximumSize(QSize(16777215, 9999999))

        self.gridLayout.addWidget(self.queryTextEdit, 1, 0, 1, 1)

        self.stqrtQueryButton = QPushButton(self.centralwidget)
        self.stqrtQueryButton.setObjectName(u"stqrtQueryButton")
        self.stqrtQueryButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.stqrtQueryButton, 3, 0, 1, 1)

        Editor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Editor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 623, 21))
        self.menu_Daten = QMenu(self.menubar)
        self.menu_Daten.setObjectName(u"menu_Daten")
        self.menu_Exportieren = QMenu(self.menu_Daten)
        self.menu_Exportieren.setObjectName(u"menu_Exportieren")
        self.menu_SQL = QMenu(self.menubar)
        self.menu_SQL.setObjectName(u"menu_SQL")
        self.menuAnsicht = QMenu(self.menubar)
        self.menuAnsicht.setObjectName(u"menuAnsicht")
        Editor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Editor)
        self.statusbar.setObjectName(u"statusbar")
        Editor.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Editor)
        self.toolBar.setObjectName(u"toolBar")
        Editor.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_Daten.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())
        self.menubar.addAction(self.menu_SQL.menuAction())
        self.menu_Daten.addAction(self.menu_Exportieren.menuAction())
        self.menu_Daten.addAction(self.action_Importieren)
        self.menu_Exportieren.addAction(self.action_xls)
        self.menu_SQL.addAction(self.actionAntworten_exportieren)
        self.menuAnsicht.addAction(self.actionSqlQuery)
        self.toolBar.addAction(self.action_anwenden)
        self.toolBar.addAction(self.action_zurueck)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_newline)
        self.toolBar.addAction(self.action_loeschen)
        self.toolBar.addSeparator()

        self.retranslateUi(Editor)

        QMetaObject.connectSlotsByName(Editor)
    # setupUi

    def retranslateUi(self, Editor):
        self.action_xls.setText(QCoreApplication.translate("Editor", u"als .xls", None))
        self.action_anwenden.setText(QCoreApplication.translate("Editor", u"\u00c4nderungen anwenden", None))
#if QT_CONFIG(tooltip)
        self.action_anwenden.setToolTip(QCoreApplication.translate("Editor", u"\u00c4nderungen \u00fcbernehmen.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_anwenden.setStatusTip(QCoreApplication.translate("Editor", u"\u00c4nderungen \u00fcbernehmen.", None))
#endif // QT_CONFIG(statustip)
        self.action_loeschen.setText(QCoreApplication.translate("Editor", u"Eintrag l\u00f6schen", None))
#if QT_CONFIG(tooltip)
        self.action_loeschen.setToolTip(QCoreApplication.translate("Editor", u"Markierten Eintrag l\u00f6schen.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_loeschen.setStatusTip(QCoreApplication.translate("Editor", u"Markierten Eintrag l\u00f6schen.", None))
#endif // QT_CONFIG(statustip)
        self.action_zurueck.setText(QCoreApplication.translate("Editor", u"R\u00fcckg\u00e4ngig", None))
#if QT_CONFIG(tooltip)
        self.action_zurueck.setToolTip(QCoreApplication.translate("Editor", u"\u00c4nderungen r\u00fcckg\u00e4ngig machen.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_zurueck.setStatusTip(QCoreApplication.translate("Editor", u"\u00c4nderungen r\u00fcckg\u00e4ngig machen.", None))
#endif // QT_CONFIG(statustip)
        self.action_newline.setText(QCoreApplication.translate("Editor", u"Neue Zeile", None))
#if QT_CONFIG(tooltip)
        self.action_newline.setToolTip(QCoreApplication.translate("Editor", u"F\u00fcgt eine neue Zeile in die Datenbank ein.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_newline.setStatusTip(QCoreApplication.translate("Editor", u"Neue Zeile am Ende der Datenbank hinzuf\u00fcgen.", None))
#endif // QT_CONFIG(statustip)
        self.actionAntworten_exportieren.setText(QCoreApplication.translate("Editor", u"Antworten exportieren", None))
#if QT_CONFIG(statustip)
        self.actionAntworten_exportieren.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.action_Importieren.setText(QCoreApplication.translate("Editor", u"Datenbank &importieren", None))
#if QT_CONFIG(tooltip)
        self.action_Importieren.setToolTip(QCoreApplication.translate("Editor", u"Importiert eine Datenbank", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Importieren.setShortcut(QCoreApplication.translate("Editor", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionSqlQuery.setText(QCoreApplication.translate("Editor", u"SQL Query", None))
        self.stqrtQueryButton.setText(QCoreApplication.translate("Editor", u"SQL QUERY", None))
        self.menu_Daten.setTitle(QCoreApplication.translate("Editor", u"&Daten", None))
        self.menu_Exportieren.setTitle(QCoreApplication.translate("Editor", u"&Exportieren", None))
        self.menu_SQL.setTitle(QCoreApplication.translate("Editor", u"SQL-Abfrage", None))
        self.menuAnsicht.setTitle(QCoreApplication.translate("Editor", u"Ansicht", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Editor", u"Werkzeugleiste", None))
        pass
    # retranslateUi

