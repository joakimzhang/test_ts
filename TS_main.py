#-*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *


import TS_UI
import os
import TS_analysis
import switch_stream
import save_data


class switch_stream_Worker(QThread):
    '''切换码流的子线程，QT中子线程内不能操作GUI界面，切记切记'''
    def __init__(self,ts_file,ts_card,parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.isWait=False
        self.data={}
        self.file = ts_file
        self.card = ts_card
    def setVar(self, name, value):
        self.data[name]=value
    def __del__(self):
 
        self.exiting = True
        self.wait()
    def run(self):
        print "I love switch,the ts path is:%s"%self.file
        argv_stream = ["-H", self.card,"-P", "7777","-f",self.file,'--std=DTMB',"-F", "522"]
        switch_stream.exec_switch(argv_stream)
        
        #switch_s.exec_switch()
        self.emit(SIGNAL('output(QString)'),self.file)
        print "switch stream"

class TS_TOOL(QDialog,TS_UI.Ui_UI_WINDOW):
    '''主函数'''
    def __init__(self,parent=None):
        super(TS_TOOL,self).__init__(parent)
        #self.__text = unicode(text)
        #self.__index = 0
        self.setupUi(self)
        self.updateUi()
        self.get_file_path()
        self.all_card = ["bjdittest","bjdittest1","bjdittest2"]
        self.ts_card = self.all_card[0]
        #self.ts_path = ""
    def updateUi(self): 
        #这个setupUi()方法会调用 QtCore.QmetaObject.connectSlotsByName()方法,这个方法的作用是它会自动创建 signal-slots connection ,这种connection是基于我们子类里的方法，和窗口的widgets之间的，只要我们定义的方法，它的名字是 on_widgetName_signalName的这种格式，就会自动把这个widgets和这个signaName connected。
        enable = not self.TS_file_lineEdit.text().isEmpty()
        print "enable is :%d"%enable
        self.Analysis_Button.setEnabled(enable)
        self.showpic_Button.setEnabled(enable)
    def on_TS_file_lineEdit_textEdited(self):
        self.__index = 0
        self.updateUi()
        self.ts_path = str(self.TS_file_lineEdit.text())
        print self.ts_path
    def Get_AV_PID(self):
        try:
            self.test_object=TS_analysis.TS_analysis(self.ts_path)
        except Exception:
            print "打开文件失败:%s"%Exception
            QMessageBox.information(self,"Information",self.tr("the audio/video pid should not be blank,should be int"))
            return 0
        test_PID=self.test_object.get_sync_head()
        print "PID:%d"%test_PID
        
        if test_PID != 0:

            self.test_object.get_PMT_PID()
            self.test_object.get_programe_PID()
    def analysis(self):
        #self.ts_path = str(self.TS_file_lineEdit.text().strip())
        self.v_pid = self.Video_pid.text()
        self.a_pid = self.Audio_pid.text()
        if self.v_pid == '' or self.a_pid == '':
            print "the v pid should be number"
            QMessageBox.information(self,"Information",self.tr("the audio/video pid should not be blank,should be int"))
            #return 0 
        print "video pid is :%s"%self.v_pid
        print "audio pid is :%s"%self.a_pid
        print self.ts_path
        '''
        try:
            self.test_object=TS_analysis.TS_analysis(self.ts_path)
        
        except Exception:
            print "can not find TS file:%s"%Exception
            QMessageBox.information(self,"Information",self.tr("Can not find the TS file"))
            return 0
        '''
        
        #test_PID=0
        test_PID=self.test_object.get_sync_head()
        print "PID:%d"%test_PID
        
        if test_PID != 0:
            print "get PID successful:%d"%test_PID
            #self.test_object.get_pid_pts(152,153)
            self.test_object.get_pid_pts(self.v_pid,self.a_pid)
            
            print "!!!!!!!!!the pts_x_y is %s!!!!!!!!!!!!!" % self.test_object.pts_x_y
            self.save_file_path()
        else:
            print "get PID fail"
        #self.test_object.show_PID_pic()
    def switch_card(self,text):
        print text
        self.ts_card = self.all_card[text]  
        print self.ts_card
    def switch_stream(self):
        #self.ts_path = str(self.TS_file_lineEdit.text().strip())
        try:
            self.ts_path
        except Exception:
            QMessageBox.information(self,"Information",self.tr("Can not find the TS file,please input the path"))
            return 0
            
        self.thread = switch_stream_Worker(self.ts_path,self.ts_card)
        self.thread.start()
        #self.thread.run(self.ts_path).start()
        #os.popen('python D:\Availink_Platform_IDE\newWorkspace_new\dweb_login\login_web\temp_test_space\switch_stream.py')
        QObject.connect(self.thread, SIGNAL(QString.fromUtf8("output(QString)")), self.switch_cmp)

    def show_pic(self):
        try:
            self.test_object.show_PID_pic()
        except Exception:
            QMessageBox.information(self,"Information",self.tr("Can not find the TS file"))
    def slotInformation(self):  
        QMessageBox.information(self,"Information",self.tr("Can not find TS file"))  
        
    def switch_cmp(self):  
        QMessageBox.information(self,"Information",self.tr("switch stream completed"))  
        
        
    def save_file_path(self):
        print self.ts_path
        key=self.ts_path.strip()
        #value={'int':12,'float':9.5,'string':'sample data'}
        #value=self.test_object.pts_x_y
        #value=self.test_object.get_programe_PID()
        value=self.test_object.program_PID
        print "value is %s"%value
        data = save_data.save_data()
        data.creat_shelf(key,value)     
        data.print_shelf(key)
        data.get_all_val()
        
    def get_file_path(self):
        
        data = save_data.save_data()
        stream_list = data.get_all_val()
        print stream_list
        self.tableWidget.setRowCount(len(stream_list))
        #self.tableWidget.setColumnCount(len(stream_list))
        
        colume = 0
        for i in stream_list:     
            self.plainTextEdit.appendPlainText(i[0].decode('utf8'))
            newItem = QTableWidgetItem(i[0].decode('utf8'))
            newItem_value = QTableWidgetItem(str(i[1]))    
            self.tableWidget.setItem(colume, 0, newItem) 
            self.tableWidget.setItem(colume, 1, newItem_value)
            colume += 1            
        #print "aaa%s"%self.TS_file_lineEdit.text
        
if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    form = TS_TOOL()
    form.show()
    app.exec_()
    #print form.text()
    
    #form = TS_analysis("text")