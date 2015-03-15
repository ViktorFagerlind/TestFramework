import os
import sys
import glob
import datetime
import threading

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

  def __init__ (self, listView, directory, filename):
    self.listView = listView
    self.modelLog = QtGui.QStandardItemModel (self.listView)
    self.listView.setModel (self.modelLog)
    self.directory = directory

    self.fileLock = threading.Lock ()
    self.currentFile = None
    self.__startFileLogging__ (filename)

  def __del__(self):
    self.__stopFileLogging__ ()

  def __startFileLogging__ (self, filename):
    self.fileLock.acquire ()
    
    if (not os.path.isdir (self.directory)):
      os.makedirs (self.directory)
    
    filepath = self.directory + filename + ".log"
    
    if (self.currentFile != None):
      Log.mainLog.putError ("Failed to open " + filepath + "- log file already open")
    else: 
      try:
        self.currentFile = open (filepath,'w')     
      except:
        Log.mainLog.putError ("Failed to open " + filepath)
        self.currentFile = None
    
    self.fileLock.release ()
  
  def __stopFileLogging__ (self):
    self.fileLock.acquire ()
    self.currentFile.close ()
    self.currentFile = None
    self.fileLock.release ()



  def appendLogLine (self, text, bold, color):
    font = QtGui.QFont("Courier New", 9, QtGui.QFont.Light)
    font.setBold (bold)

    item = QtGui.QStandardItem (text)
    item.setFont (font)
    item.setForeground (QtGui.QColor(color))

    self.modelLog.appendRow (item)

  def newline (self):
    self.appendLogLine ("", False, "black")

  def putSuccessFail (self, text, success):
    self.put (text, True, "green" if success else "red")

  def putError (self, text):
    self.put (text, False, "red")

  def put (self, text, bold = False, color = "black", timeStamp = True):
    text = (("[" + Settings.getSmallNowString () + "] ") if timeStamp else "") + text
    self.appendLogLine (text, bold, color)

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
        
    self.put (line, False, "black", False)

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

    Log.mainLog = LogManager.addLog ("System", Settings.resultFolder, "System")

  @staticmethod
  def closeTab (currentIndex):
    if (currentIndex == 0):
      Log.mainLog.putError ("Cannot close the system log")
      return

    LogManager.tabWidget.removeTab (currentIndex)

  @staticmethod

  def addLog (name, directory, filename):
    listView = QtGui.QListView (LogManager.tabWidget)
    LogManager.tabWidget.addTab (listView, name)
    LogManager.tabWidget.setCurrentWidget (listView)

    return Log (listView, directory, filename)
