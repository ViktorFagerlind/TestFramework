import sys

from Log import Log
from TestManager import TestManager
from PySide import QtGui
from MainWindow import Ui_MainWindow

class ControlMainWindow (QtGui.QMainWindow):
  def __init__ (self, parent=None):
    super (ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow ()
    self.ui.setupUi (self)

    # Connect actions
    self.ui.actionQuit.triggered.connect  (ControlMainWindow.Quit)

    # Init log list view
    self.modelLog = QtGui.QStandardItemModel (self.ui.listViewLog)
    self.ui.listViewLog.setModel (self.modelLog)
    
    # Init TestManager
    self.TestManager = TestManager (self.ui.tabWidgetTest, self.ui.actionStart, self.ui.actionAbort)

    # Init log
    Log.setLoggingFunction (self.appendLogLine)
    Log.put ("Ready!")

  def appendLogLine (self, text):
#    font = QtGui.QFont('Courier New', 9, QtGui.QFont.Light)
    item = QtGui.QStandardItem (text)
#    item.setFont (font)
    self.modelLog.appendRow (item)
    
  @staticmethod
  def Quit ():
    QtGui.qApp.closeAllWindows ()
  
if __name__ == "__main__":
    app = QtGui.QApplication (sys.argv)
    mySW = ControlMainWindow ()
    mySW.show ()
    sys.exit (app.exec_ ())