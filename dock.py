# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.createDockWindows()
        
    def createDockWindows(self):
        dock1 = QtGui.QDockWidget('Tab1', self)
        dock1.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        widget1 = QtGui.QWidget(parent=dock1)
        dock1.setWidget(widget1)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock1)
        
        dock2 = QtGui.QDockWidget('Tab2', self)
        dock2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        widget2 = QtGui.QWidget(parent=dock1)
        dock2.setWidget(widget2)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock2)
        
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())