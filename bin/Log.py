import threading
import sys

from PySide import QtGui

class Settings:
  resultFolder = "../results/"
  testPath = "../tests/"
  inputPath = "../input/"

class Log:
  noBefore   = 5
  lineLength = 80
  filler     = '='

  mainLog = None

  def __init__ (self, logFunction, isMain, listView):
    self.listView = listView
    self.modelLog = QtGui.QStandardItemModel (self.listView)
    self.listView.setModel (self.modelLog)

    self.fileLock = threading.Lock ()

    if isMain:
      Log.mainLog = self

    self.currentFile = None

  def startFileLogging (self, name):
    self.fileLock.acquire ()
    
    filepath = Settings.resultFolder + name + ".log"
    
    if (self.currentFile != None):
      print ("Failed to open " + filepath + "- log file already open")
    else: 
      try:
        self.currentFile = open (filepath,'w')     
      except:
        print ("Failed to open " + filepath)
        self.currentFile = None
    
    self.fileLock.release ()
  
  def stopFileLogging (self):
    #print (self, "current file: " + str (self, self.currentFile))
    self.fileLock.acquire ()
    self.currentFile.close ()
    self.currentFile = None
    self.fileLock.release ()
  
  def appendLogLine (self, text):
    item = QtGui.QStandardItem (text)

    font = QtGui.QFont('Courier New', 9, QtGui.QFont.Light)
    item.setFont (font)

    self.modelLog.appendRow (item)

  def put (self, text):
    self.appendLogLine (text)
    
    self.fileLock.acquire ()
    if (self.currentFile != None):
      self.currentFile.write (text + "\n")
    self.fileLock.release ()

  def largeHeading (self, name):
    self.lineHeading ("", self.lineLength)
    self.lineHeading (name, self.lineLength)
    self.lineHeading ("", self.lineLength)

  def mediumHeading (self, name):
    self.lineHeading (name, self.lineLength)
   
  def smallHeading (self, name):
    self.lineHeading (name, self.lineLength//2 + 10)
    
  def lineHeading (self, name, length):
    line = "".join (self.filler for i in range(self.noBefore)) 

    if (len (name) != 0):
      line += self.extend (" " + name + " ", length - len (line), self.filler)
    else:
      line += self.extend ("", length - len (line), self.filler)
        
    self.put (line)

  @staticmethod
  def getSuccessFailed (isSuccess):
    if (isSuccess):
      return "Success"
    else:
      return "Failed"

  @staticmethod
  def extend (name, length, char):
    line = name
    currentLength = len (line)
    line += "".join (char for i in range(length - currentLength))
    return line    

class LogManager:
  tabWidget = None

  @staticmethod
  def setup (tabWidget):
    LogManager.tabWidget = tabWidget
    LogManager.tabWidget.setTabsClosable (True)
    LogManager.tabWidget.tabCloseRequested.connect (LogManager.closeTab)

    LogManager.__addLog__ (True, "Main")

  @staticmethod
  def addLog (name):
    return LogManager.__addLog__ (False, name)

  @staticmethod
  def closeTab (currentIndex):
    if (currentIndex == 0):
      Log.mainLog.put ("Cannot close the main log")
      return

    LogManager.tabWidget.removeTab (currentIndex)

  @staticmethod
  def __addLog__ (isMain, name):
    listView = QtGui.QListView (LogManager.tabWidget)
    LogManager.tabWidget.addTab (listView, name)
    LogManager.tabWidget.setCurrentWidget (listView)

    return Log (isMain, name, listView)
