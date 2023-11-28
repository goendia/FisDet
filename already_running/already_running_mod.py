__author__ = 'chris'

# only needed for python2
import sip
sip.setapi('QString', 2)

from PyQt4 import QtGui, QtCore, QtNetwork

class SingleApplication(QtGui.QApplication):

    def __init__(self, argv, key):
        QtGui.QApplication.__init__(self, argv)
        self._memory = QtCore.QSharedMemory(self)
        self._memory.setKey(key)
        if self._memory.attach():
            self._running = True
        else:
            self._running = False
            if not self._memory.create(1):
                raise RuntimeError(self._memory.errorString())

    def isRunning(self):
        return self._running


if __name__ == '__main__':

    import sys

    key = 'app-name'


    app = SingleApplication(sys.argv, key)
    if app.isRunning():
        print('app is already running')
        sys.exit(1)

    window = Window()
    window.show()

    sys.exit(app.exec_())
