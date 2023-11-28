# -*- coding: utf-8 -*-

__author__ = 'chris'

from PySide6.QtGui import QMessageBox, QApplication
from PySide6.QtCore import QIODevice, QTimer
from PySide6.QtNetwork import QLocalServer, QLocalSocket
import sys

class QSingleApplication(QApplication):
    def singleStart(self, mainWindow):
        self.mainWindow = mainWindow
        # Socket
        self.m_socket = QLocalSocket()
        self.m_socket.connected.connect(self.connectToExistingApp)
        self.m_socket.error.connect(self.startApplication)
        self.m_socket.connectToServer(self.applicationName(), QIODevice.WriteOnly)
    def connectToExistingApp(self):
        if len(sys.argv)>1 and sys.argv[1] is not None:
            self.m_socket.write(sys.argv[1])
            self.m_socket.bytesWritten.connect(self.quit)
        else:
            ########### habe self.tr() vor den Textpassagen der MessageBox entfernt, hat anscheinend keine Auswirkungen...
            QMessageBox.warning(None, (u"Läuft bereits"), ("Eine Instanz von Fisdet ist noch ge"+u'ö'+"ffnet.\n\n Bitte zuerst schlie"+u'ß'+"en."))
            # Quit application in 250 ms
            QTimer.singleShot(250, self.quit)
    def startApplication(self):
        self.m_server = QLocalServer()
        if self.m_server.listen(self.applicationName()):
            self.m_server.newConnection.connect(self.getNewConnection)
            self.mainWindow.show()
        else:
            QMessageBox.critical(None, self.tr("Error"), self.tr("Error listening the socket."))
    def getNewConnection(self):
        self.new_socket = self.m_server.nextPendingConnection()
        self.new_socket.readyRead.connect(self.readSocket)
    def readSocket(self):
        f = self.new_socket.readLine()
        self.mainWindow.getArgsFromOtherInstance(str(f))
        self.mainWindow.activateWindow()
        self.mainWindow.show()
