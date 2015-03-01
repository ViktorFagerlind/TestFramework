import sys
import glob

from PySide import QtGui
from Log import Settings

# ---- TestCollection --------------------------------------------------------------------------------------------------

class TestCollection ():
  tests = {}

  @staticmethod
  def readTests ():
    TestCollection.tests.clear ()

    sys.path.append (Settings.testPath)
    fileNames = glob.glob (Settings.testPath + "*.py")
    for fn in fileNames:
      splitName = fn.split('\\')
      fileName = splitName[len (splitName)-1]
      testClassName = fileName[0:(len (fileName)-3)]
      TestCollection.appendTest (testClassName)

  @staticmethod
  def appendTest (testClassName):
    testModule = __import__ (testClassName)
    testClass = getattr (testModule, testClassName)
    testInstance = testClass ()
    testName = testInstance.name
    TestCollection.tests[testName] = testClass

  @staticmethod
  def getTestClass (name):
    return TestCollection.tests[name]

  @staticmethod
  def getTestNames ():
    names = TestCollection.tests.keys ()
    names.sort ()
    return names

  @staticmethod
  def runTest (name):
    testClass = TestCollection.getTestClass (name)
    testInstance = testClass ()
    print ("Starting " + name)
    testInstance.run ()

# ---- TestSet ---------------------------------------------------------------------------------------------------------

class TestSet ():
  def __init__ (self, name, listView):
    self.name  = name
    self.testNames = []

    # Init test list view
    self.listView = listView
    self.modelTests = QtGui.QStandardItemModel (self.listView)
    self.listView.setModel (self.modelTests)

  def addTests (self, names):
    self.testNames.extend (names)
    self.refreshGui ()

  def refreshGui (self):
    self.modelTests.clear ()
    for tn in self.testNames:
      item = QtGui.QStandardItem (tn)
      self.modelTests.appendRow (item)

  def Start (self):
    selectedItems = self.listView.selectedIndexes ()
    if (len (selectedItems) == 0):
      print ("No test selected!")
      return
    TestCollection.runTest (selectedItems[0].data ())

# ---- TestManager -----------------------------------------------------------------------------------------------------

class TestManager:
  def __init__ (self, tabWidget, actionStart, actionAbort):
    self.tabWidget = tabWidget

    actionStart.triggered.connect  (self.Start)
    actionAbort.triggered.connect  (TestManager.Abort)

    # Init TestCollection
    TestCollection.readTests ()

    #Add TestCollection All Tests
    listView = QtGui.QListView(self.tabWidget)
    setAllTests = TestSet ("All Tests", listView)
    setAllTests.addTests (TestCollection.getTestNames ())
    self.tabWidget.addTab (listView, setAllTests.name)

    self.sets = []
    self.sets.append (setAllTests)

  def Start (self):
    self.sets[0].Start ()

  @staticmethod
  def Abort ():
    print ("Abort")




