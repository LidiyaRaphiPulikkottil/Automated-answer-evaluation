import sys
import project
import Tkinter
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import (
     QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
     QFrame, QGridLayout, QVBoxLayout,
     )


class Window(QtGui.QMainWindow):

    def __init__(self):
        

        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("DESCRIPTIVE ANSWER EVALUATION SYSTEM")
        self.but()

        extract=QtGui.QAction("&New",self)
        extract.setShortcut("Ctrl+N")
        extract.setStatusTip('New file')
        extract.triggered.connect(self.SingleBrowse)

               


        
        self.statusBar()

        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('&File')
        fileMenu.addAction(extract)

        runner=QtGui.QAction("&Run",self)
        runner.setShortcut("Ctrl+R")
        runner.setStatusTip('Run program')
        runner.triggered.connect(self.main_pro)
        fileMenu.addAction(runner)

    def but(self):
             


        btn = QtGui.QPushButton('Select file', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
        btn.move(200,150)
        

     


        self.show()

    def SingleBrowse(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self,'Single File',"~/Desktop/PyRevolution/PyQt4",'*.txt')
        file1=open(filePath,'r')
        #print filePath
        filePath=str(filePath)
        pos=filePath.find("ans",0,len(filePath))
        #print pos
        sub=filePath[pos:]
        #print sub
        file2=open('abc.txt','w')
        file2.write(sub)
    


        
        file=open('text.txt','w')
        lines=file1.readlines()
        for line in lines:
            file.write(line)
        file.close
        file1.close
        

        
        

    def editor(self):
        self.textEdit=QtGui.QLineEdit()
        self.setCentralWidget(self.textEdit)




    def main_pro(self):
        
        reload(project)
        project.main()
        self.file_open()
        


    def file_open(self):
        file=open('res.txt','r')
        self.editor()
        with file:
            text=file.read()
            self.textEdit.setText(text)       
                
app=QtGui.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())

                                            
