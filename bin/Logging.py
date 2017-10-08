import os
import sys
import glob
import datetime
#import threading
import logging

from PySide import QtGui

class Settings:
  resultFolder = "../results/"
  testPath = "../tests/"
  inputPath = "../input/"
  
  @staticmethod
  def getNowString ():
    nowString = str (datetime.datetime.now()).replace (':','.')
    return nowString[0:len (nowString)-3]

  @staticmethod
  def getSmallNowString ():
    nowString = str (datetime.datetime.now())
    return nowString[11:22]

  @staticmethod
  def getFilenamesFromDir (wildcard, dir):
    result = []
    sys.path.append (dir)
     
    fileNames = glob.glob (dir + wildcard)
    for fn in fileNames:
      splitName = fn.split('\\')
      result.append (splitName[len (splitName)-1])
    
    return result
      
  @staticmethod
  def getDirsFromDir (dir):
    result = []
    for fd in os.listdir (dir):
      path = dir + str (fd)
      if os.path.isdir (path):
        result.append (str (fd))
    return result

class Log:
  noBefore   = 5
  lineLength = 80
  filler     = '='

  mainLog = None

  def __init__ (self, logger):
    self.logger = logger

  def newline (self):
    self.put ("", False, "black")

  # TODO
  def putSuccessFail (self, text, success):
    self.put (text, True, "green" if success else "red")

  def putError (self, text):
    self.put (text, False, "red")

  def put (self, text, bold = False, color = "black"):
    self.logger.info (text)

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
        
    self.put (line, False)

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
  def setup (tabWidget, actionCloseLogs):
    LogManager.tabWidget = tabWidget
    LogManager.tabWidget.setTabsClosable (True)
    LogManager.tabWidget.tabCloseRequested.connect (LogManager.closeTab)
    actionCloseLogs.triggered.connect (LogManager.closeAllTabs)

    logging.getLogger().setLevel(logging.DEBUG)


    Log.mainLog = LogManager.addLog ("System", Settings.resultFolder, "System")

  @staticmethod
  def closeTab (currentIndex):
    if (currentIndex == 0):
      Log.mainLog.putError ("Cannot close the system log")
      return

    LogManager.tabWidget.removeTab (currentIndex)

  @staticmethod
  def closeAllTabs ():
    for i in range(LogManager.tabWidget.count()-1):
      LogManager.tabWidget.removeTab (1)

  @staticmethod
  def addLog (name, directory, filename):

    listView = QtGui.QListView (LogManager.tabWidget)
    LogManager.tabWidget.addTab (listView, name)
    LogManager.tabWidget.setCurrentWidget (listView)
    
    listViewHandler = ListViewLogger (listView)
    listViewHandler.setLevel (logging.INFO)
    listViewHandler.setFormatter (logging.Formatter('[%(asctime)s.%(msecs)03d] %(message)s', '%H:%M:%S'))

    if not os.path.exists(directory):
      os.makedirs(directory)
    fileHandler = logging.FileHandler (directory + filename + ".log")
    fileHandler.setLevel (logging.DEBUG)
    fileHandler.setFormatter (logging.Formatter('[%(asctime)s.%(msecs)03d] %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S'))
    
    logger = logging.getLogger (name)
    logger.addHandler (listViewHandler)
    logger.addHandler (fileHandler)

    logger.propagate = False
    
    return Log (logger)
  
  @staticmethod
  def getStandaloneLog (name):
    logging.basicConfig (level=logging.DEBUG, format='%(message)s')
  
    return Log (logging.getLogger ())

class ListViewLogger (logging.Handler):
  def __init__(self, listView):
    super().__init__()
    
    self.listView = listView
    self.modelLog = QtGui.QStandardItemModel (self.listView)
    self.listView.setModel (self.modelLog)
    
    self.font = QtGui.QFont("Courier New", 9, QtGui.QFont.Light)
    #self.font.setBold (bold)
    
  def emit(self, record):
    line = self.format(record)
    item = QtGui.QStandardItem (line)
    item.setFont (self.font)
    #item.setForeground (QtGui.QColor(color))
    self.modelLog.appendRow (item)

  def write(self, m):
      pass

class StreamToLog(object):
  def __init__(self, log, isErr=False):
    self.log   = log
    self.isErr = isErr

  def write(self, buf):
    for line in buf.rstrip().splitlines():
      if self.isErr:
        self.log.putError (line.rstrip())
      else:
        self.log.put (line.rstrip())
