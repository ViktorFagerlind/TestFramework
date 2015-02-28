import sys
import glob

from Log import Log
from PySide import QtCore, QtGui
from MainWindow import Ui_MainWindow

# pyside-uic MainWindow.ui -o MainWindow.py

class TestCollection ():
  def __init__ (self):
    self.tests = {}
    
  def addTest (self, name, testClass):
    self.tests[name] = testClass
    
  def getTest (self, name):
    return self.tests[name]
    
  def runTest (self, name):
    testClass = self.getTest (name)
    testInstance = testClass ()
    print ("Starting " + name)
    testInstance.run ()

class ControlMainWindow (QtGui.QMainWindow):
  def __init__ (self, parent=None):
    super (ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow ()
    self.ui.setupUi (self)

    # Connect actions
    self.ui.actionQuit.triggered.connect  (ControlMainWindow.Quit)
    self.ui.actionStart.triggered.connect (self.Start)
    self.ui.actionAbort.triggered.connect (ControlMainWindow.Abort)
    
    # Init log list view
    self.modelLog = QtGui.QStandardItemModel (self.ui.listViewLog)
    self.ui.listViewLog.setModel (self.modelLog)
    
    # Init test list view
    self.modelTests = QtGui.QStandardItemModel (self.ui.listViewTests)
    self.ui.listViewTests.setModel (self.modelTests)
    
    self.testCollection = TestCollection ()

    testPath = "../tests"
    sys.path.append (testPath)
    fileNames = glob.glob (testPath + "/*.py")
    for fn in fileNames:
      splitName = fn.split('\\')
      fileName = splitName[len (splitName)-1]
      testClassName = fileName[0:(len (fileName)-3)]
      self.__appendTest__ (testClassName)      
      
    # Init log
    Log.setLoggingFunction (self.appendLogLine)
    Log.put ("Ready!")
    
  def __appendTest__ (self, testClassName):
    testModule = __import__ (testClassName)
    testClass = getattr (testModule, testClassName)
    testInstance = testClass ()
    testName = testInstance.name
    self.testCollection.addTest (testName, testClass)
    
    item = QtGui.QStandardItem (testName)
    self.modelTests.appendRow (item)  

  def appendLogLine (self, text):
#    font = QtGui.QFont('Courier New', 9, QtGui.QFont.Light)
    item = QtGui.QStandardItem (text)
#    item.setFont (font)
    self.modelLog.appendRow (item)
    
  @staticmethod
  def Quit ():
    QtGui.qApp.closeAllWindows ()
  
  #@staticmethod
  def Start (self):
    selectedItems = self.ui.listViewTests.selectedIndexes ()
    if (len (selectedItems) == 0):
      print ("No test selected!")
      return
    self.testCollection.runTest (selectedItems[0].data ())
    
  
  @staticmethod
  def Abort ():
    print ("Abort")
  
if __name__ == "__main__":
    app = QtGui.QApplication (sys.argv)
    mySW = ControlMainWindow ()
    mySW.show ()
    sys.exit (app.exec_ ())