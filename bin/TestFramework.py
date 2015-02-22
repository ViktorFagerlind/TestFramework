import sys
import glob

from PySide import QtCore, QtGui
from MainWindow import Ui_MainWindow

# pyside-uic MainWindow.ui -o MainWindow.py

class TestCollection ():
  def __init__ (self):
    self.tests = {}
    
  def addTest (self, name, test):
    self.tests[name] = test
    
  def getTest (self, name):
    return self.tests[name]
    
  def runTest (self, name):
    testClass = self.getTest (name)
    testInstance = testClass ()
    print ("Starting " + testInstance.name)
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
    
    # Init test list view
    self.model = QtGui.QStandardItemModel (self.ui.listViewTests)
    self.ui.listViewTests.setModel (self.model)
    
    self.testCollection = TestCollection ()

    testPath = "../tests"
    sys.path.append (testPath)
    fileNames = glob.glob (testPath + "/*.py")
    for fn in fileNames:
      splitName = fn.split('\\')
      fileName = splitName[len (splitName)-1]
      name = fileName[0:(len (fileName)-3)]
      self.__appendTest__ (name)
      
     
#    modulist.append(getattr(__import__(fl[i]),fl[i]))
#    adapters.append(modulist[i]())
      
    
  def __appendTest__ (self, testName):
    item = QtGui.QStandardItem (testName)
    self.model.appendRow (item)
    
    testModule = __import__ (testName)
    testClass = getattr (testModule, testName)
    self.testCollection.addTest (testName, testClass)
    
  @staticmethod
  def Quit ():
    QtGui.qApp.closeAllWindows()
  
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