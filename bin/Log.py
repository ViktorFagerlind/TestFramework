import threading
import sys

class Settings:
  resultFolder = "../results/"

class Log:
  noBefore   = 5
  lineLength = 80
  filler     = '='
  fileLock   = threading.Lock ()
  currentFile = None
  logFunction = None

  @staticmethod
  def setLoggingFunction (logFun):
    Log.logFunction = logFun
  
  @staticmethod
  def startFileLogging (name):
    Log.fileLock.acquire ()
    
    filepath = Settings.resultFolder + name + ".log"
    
    if (Log.currentFile != None):
      print ("Failed to open " + filepath + "- log file already open")
    else: 
      try:
        Log.currentFile = open (filepath,'w')     
      except:
        print ("Failed to open " + filepath)
        Log.currentFile = None
    
    Log.fileLock.release ()
  
  @staticmethod
  def stopFileLogging ():
    #print ("current file: " + str (Log.currentFile))
    Log.fileLock.acquire ()
    Log.currentFile.close ()
    Log.currentFile = None
    Log.fileLock.release ()
  
  @staticmethod
  def put (text):
    if (Log.logFunction == None):
      sys.stdout.write (text + "\n")
    else:
      Log.logFunction (text)
    
    Log.fileLock.acquire ()
    if (Log.currentFile != None):
      Log.currentFile.write (text + "\n")
    Log.fileLock.release ()

  @staticmethod
  def largeHeading (name):
    Log.lineHeading ("", Log.lineLength)
    Log.lineHeading (name, Log.lineLength)
    Log.lineHeading ("", Log.lineLength)

  @staticmethod
  def mediumHeading (name):
    Log.lineHeading (name, Log.lineLength)
   
  @staticmethod
  def smallHeading (name):
    Log.lineHeading (name, Log.lineLength//2 + 10)
    
  @staticmethod
  def lineHeading (name, length):
    line = "".join (Log.filler for i in range(Log.noBefore)) 

    if (len (name) != 0):
      line += Log.extend (" " + name + " ", length - len (line), Log.filler)
    else:
      line += Log.extend ("", length - len (line), Log.filler)
        
    Log.put (line)

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
