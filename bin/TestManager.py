import sys
import glob
import xml.etree.ElementTree as ET

from PySide import QtGui
from Log import Log, Settings

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

# ---- TestRun ---------------------------------------------------------------------------------------------------------

class TestRun ():
  def __init__ (self, testName, instanceName):
    self.testName     = testName
    self.instanceName = instanceName

  def getName (self):
    return self.testName + " (" + self.instanceName + ")"

# ---- TestSet ---------------------------------------------------------------------------------------------------------

class TestSet ():
  def __init__ (self, name, listView):
    self.name  = name
    self.testRuns = []

    # Init test list view
    self.listView = listView
    self.modelTests = QtGui.QStandardItemModel (self.listView)
    self.listView.setModel (self.modelTests)

  def addTests (self, runs):
    self.testRuns.extend (runs)
    self.refreshGui ()

  def refreshGui (self):
    self.modelTests.clear ()
    for tr in self.testRuns:
      item = QtGui.QStandardItem (tr.getName ())
      self.modelTests.appendRow (item)

  def Start (self):
    selectedItems = self.listView.selectedIndexes ()
    if (len (selectedItems) != 1):
      Log.put ("No test selected!")
      return
    TestCollection.runTest (self.testRuns[selectedItems[0].row ()].testName)

# ---- TestManager -----------------------------------------------------------------------------------------------------

class TestManager:
  def __init__ (self, tabWidget, actionStart, actionAbort):
    self.tabWidget = tabWidget

    actionStart.triggered.connect  (self.Start)
    actionAbort.triggered.connect  (TestManager.Abort)

    # Init TestCollection
    TestCollection.readTests ()

    self.sets = []

    #Add TestCollection All Tests
    allTestsNominal = []
    for tn in TestCollection.getTestNames ():
      allTestsNominal.append (TestRun (tn, "Nominal"))
    self.AddTestSet ("All Tests", allTestsNominal)

    # Add test sets according to XML input
    tree = ET.parse (Settings.inputPath + "test_sets.xml")
    root = tree.getroot ()
    for set in root.findall ("TestSet"):
      testRuns = []
      tests = set.findall ("TestRun")
      for t in tests:
        testRuns.append (TestRun (t.get ("test"), t.get ("instance")))
      self.AddTestSet (set.get ("name"), testRuns)


  def AddTestSet (self, name, testNames):
    listView = QtGui.QListView(self.tabWidget)
    testSet = TestSet (name, listView)
    testSet.addTests (testNames)
    self.tabWidget.addTab (listView, name)
    self.sets.append (testSet)

  def Start (self):
    self.sets[self.tabWidget.currentIndex ()].Start ()

  @staticmethod
  def Abort ():
    print ("Abort")




