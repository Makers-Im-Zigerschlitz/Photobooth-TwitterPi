# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import mainwindow_auto

class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
 # access variables inside of the UI's file
 
 ### functions for the buttons to call
 def pressedbtnPicNo(self):
     global yesno
     yesno = False
     form.close()
 
 def pressedbtnPicYes(self):
     global yesno
     yesno = True
     form.close()
 
 def __init__(self):
     super(self.__class__, self).__init__()
     self.setupUi(self) # gets defined in the UI file
 
     ### Hooks to for buttons
     self.btnPicYes.clicked.connect(lambda: self.pressedbtnPicYes())
     self.btnPicNo.clicked.connect(lambda: self.pressedbtnPicNo())
 
# I feel better having one of these
def showWindow():
 # a new app instance
 app = QApplication(sys.argv)
 global form
 form = MainWindow()
 form.showFullScreen()
 print("Set fullscreen!")
 form.show()
 # without this, the script exits immediately.
 # sys.exit(app.exec_())
 app.exec_()
 print("Window closed!")
 return yesno
