# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TS_analysis_02.ui'
#
# Created: Wed Jul 15 18:19:15 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UI_WINDOW(object):
    def setupUi(self, UI_WINDOW):
        UI_WINDOW.setObjectName(_fromUtf8("UI_WINDOW"))
        UI_WINDOW.resize(460, 394)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(UI_WINDOW)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(UI_WINDOW)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.TS_file_lineEdit = QtGui.QLineEdit(UI_WINDOW)
        self.TS_file_lineEdit.setObjectName(_fromUtf8("TS_file_lineEdit"))
        self.gridLayout.addWidget(self.TS_file_lineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lineEdit_2 = QtGui.QLineEdit(UI_WINDOW)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtGui.QLineEdit(UI_WINDOW)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_2 = QtGui.QCheckBox(UI_WINDOW)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(UI_WINDOW)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(UI_WINDOW)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(UI_WINDOW)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtGui.QTableWidget(UI_WINDOW)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.plainTextEdit = QtGui.QPlainTextEdit(UI_WINDOW)
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setUndoRedoEnabled(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(UI_WINDOW)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Analysis_Button = QtGui.QPushButton(UI_WINDOW)
        self.Analysis_Button.setObjectName(_fromUtf8("Analysis_Button"))
        self.verticalLayout_2.addWidget(self.Analysis_Button)
        self.dockWidget_2 = QtGui.QDockWidget(UI_WINDOW)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.verticalLayout_2.addWidget(self.dockWidget_2)
        self.close_Button = QtGui.QPushButton(UI_WINDOW)
        self.close_Button.setObjectName(_fromUtf8("close_Button"))
        self.verticalLayout_2.addWidget(self.close_Button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.label.setBuddy(self.TS_file_lineEdit)
        self.label_3.setBuddy(self.comboBox)

        self.retranslateUi(UI_WINDOW)
        #QtCore.QObject.connect(self.Analysis_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), UI_WINDOW.analysis)
        #QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(int)")), UI_WINDOW.switch_card)
        #QtCore.QMetaObject.connectSlotsByName(UI_WINDOW)

    def retranslateUi(self, UI_WINDOW):
        UI_WINDOW.setWindowTitle(_translate("UI_WINDOW", "Dialog", None))
        self.label.setText(_translate("UI_WINDOW", "TS文件", None))
        self.checkBox_2.setText(_translate("UI_WINDOW", "CheckBox1", None))
        self.checkBox.setText(_translate("UI_WINDOW", "CheckBox2", None))
        self.label_3.setText(_translate("UI_WINDOW", "常用server", None))
        self.comboBox.setItemText(0, _translate("UI_WINDOW", "Bjdevel03", None))
        self.comboBox.setItemText(1, _translate("UI_WINDOW", "Bjserver3", None))
        self.comboBox.setItemText(2, _translate("UI_WINDOW", "Bjfile02", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UI_WINDOW", "文件", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UI_WINDOW", "属性", None))
        self.Analysis_Button.setText(_translate("UI_WINDOW", "Analysis_Button", None))
        self.close_Button.setText(_translate("UI_WINDOW", "close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UI_WINDOW = QtGui.QDialog()
    ui = Ui_UI_WINDOW()
    ui.setupUi(UI_WINDOW)
    UI_WINDOW.show()
    sys.exit(app.exec_())

