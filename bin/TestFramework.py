import sys

from ResultTreeModel  import ResultTreeModel
from Logging              import Log, LogManager
from TestManager      import TestManager
from Results       import TestResultManager
from PySide           import QtGui
from MainWindow       import Ui_MainWindow

class ControlMainWindow (QtGui.QMainWindow):
  def __init__ (self, parent=None):
    super (ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow ()
    self.ui.setupUi (self)

    # Connect actions
    self.ui.actionQuit.triggered.connect  (ControlMainWindow.Quit)

    # Init log
    LogManager.setup (self.ui.tabWidgetLog)

    Log.mainLog.put ("Ready!")
    
    # Init TestManager
    self.TestManager = TestManager (self.ui.tabWidgetTest,
                                    self.ui.actionStartSet,
                                    self.ui.actionStartTest,
                                    self.ui.actionAbort)

    # Init TestResultManager
    self.resultTreeModel = ResultTreeModel (self.ui.TreeViewResults, self.ui.actionTestResultsClicked)
    self.ui.TreeViewResults.setModel (self.resultTreeModel)
    self.ui.TreeViewResults.setAlternatingRowColors(True)

    TestResultManager.setup (self.resultTreeModel)

  @staticmethod
  def Quit ():
    QtGui.qApp.closeAllWindows ()
  
if __name__ == "__main__":
    app = QtGui.QApplication (sys.argv)
    mySW = ControlMainWindow ()
    mySW.show ()
    sys.exit (app.exec_ ())
