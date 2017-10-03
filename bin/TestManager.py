import sys
import xml.etree.ElementTree as ET

from Results import TestResultManager, SetResult
from PySide     import QtGui
from Logging        import Log, Settings

# ---- TestCollection --------------------------------------------------------------------------------------------------

class TestConfiguration ():
  testConfigXmlRoot = None

  @staticmethod
  def readConfigurations ():
    xml = ET.parse (Settings.inputPath + "test_configurations.xml")
    TestConfiguration.testConfigXmlRoot = xml.getroot ()

  @staticmethod
  def getValueString (testName, instanceName, parameterName):
    instanceRoot = TestConfiguration.getInstanceRoot (testName, instanceName)
    if instanceRoot is None:
      return None
    param = instanceRoot.find (parameterName)
    if param is None:
      return None
    return param.text

  @staticmethod
  def getInstances (testName):
    instances = []
    for t in TestConfiguration.testConfigXmlRoot.findall("Test"):
      if (t.get ("name") == testName):
        for i in t.findall("Instance"):
          instances.append (i.get ("name"))
      
    if not instances:
      instances.append ("Default")
      
    return instances

  @staticmethod
  def getInstanceRoot (testName, instanceName):
    for t in TestConfiguration.testConfigXmlRoot.findall("Test"):
      if (t.get ("name") == testName):
        for i in t.findall("Instance"):
          if (i.get ("name") == instanceName):
            return i
    return None


class TestCollection ():
  tests = {}

  @staticmethod
  def readTests ():
    TestCollection.tests.clear ()

    # Add tests directory to the path in order to be able to import the test classes
    sys.path.append (Settings.testPath)
    
    fileNames = Settings.getFilenamesFromDir ("*.py", Settings.testPath)
    for fn in fileNames:
      testClassName = fn[0:(len (fn)-3)]
      TestCollection.appendTest (testClassName)

  @staticmethod
  def appendTest (testClassName):
    testModule = __import__ (testClassName)
    testClass = getattr (testModule, testClassName)
    testInstance = testClass ("")
    testName = testInstance.name
    TestCollection.tests[testName] = testClass

  @staticmethod
  def getTestClass (name):
    return TestCollection.tests[name]

  @staticmethod
  def getTestNames ():
    names = TestCollection.tests.keys ()
    return sorted (names)

  @staticmethod
  def runTest (testRun, testResultSet):
    testClass = TestCollection.getTestClass (testRun.testName)
    testInstance = testClass (testRun.instanceName)
    testInstance.run (testResultSet)

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
    Log.mainLog.put ("Start set: " + self.name)

    setResult = SetResult (self.name + " - " + Settings.getNowString ())
  
    for tr in self.testRuns:
      TestCollection.runTest (tr, setResult)
      
    TestResultManager.addSetResult (setResult)

  def StartSingleTest (self):
    selectedItems = self.listView.selectedIndexes ()
    if (len (selectedItems) != 1):
      Log.mainLog.put ("No test selected!")
      return
    TestCollection.runTest (self.testRuns[selectedItems[0].row ()], TestResultManager.singleRunSet)

# ---- TestManager -----------------------------------------------------------------------------------------------------

class TestManager:
  def __init__ (self, tabWidget, actionStartSet, actionStartTest, actionAbort):
    self.tabWidget = tabWidget

    actionStartTest.triggered.connect  (self.StartTest)
    actionStartSet.triggered.connect  (self.StartSet)
    actionAbort.triggered.connect  (TestManager.Abort)

    # Init Test configurations
    TestConfiguration.readConfigurations ()

    # Init TestCollection
    TestCollection.readTests ()

    self.sets = []
    #Add TestCollection All Tests
    allTestsNominal = []
    for tn in TestCollection.getTestNames ():
      for i in TestConfiguration.getInstances (tn):
        allTestsNominal.append (TestRun (tn, i))
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

  def StartTest (self):
    self.sets[self.tabWidget.currentIndex ()].StartSingleTest ()

  def StartSet (self):
    self.sets[self.tabWidget.currentIndex ()].Start ()

  @staticmethod
  def Abort ():
    Log.mainLog.put ("Abort")
