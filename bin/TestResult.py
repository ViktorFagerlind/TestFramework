import pickle
import datetime
import time
import os
import sys

from Log import Log
from Log import Settings

class TestResultManager:
  singleRunSet = None
  setResults = []
  
  @staticmethod
  def setup ():
    TestResultManager.singleRunSet = SetResult ("SingleTestRuns")
    TestResultManager.addSetResult (TestResultManager.singleRunSet)
    
    TestResultManager.readFromDisk ()
    TestResultManager.printContents ()

  @staticmethod
  def getSetResult (setResultName):
    for tr in TestResultManager.setResults:
      if (tr.name == setResultName):
        return tr
    return None
  
  @staticmethod
  def getOrCreateSetResult (setResultName):
    result = TestResultManager.getSetResult (setResultName)
    if (result == None):
      result = SetResult (setResultName)
      TestResultManager.setResults.append (result)
    return result
  
  @staticmethod
  def readFromDisk ():
    setResultDirs = Settings.getDirsFromDir (Settings.resultFolder)
    
    for d in setResultDirs:
      setResult = TestResultManager.getOrCreateSetResult (d)
      testResultFiles = Settings.getFilenamesFromDir ("*.rslt", Settings.resultFolder + d + "/")

      for fn in testResultFiles:
        testResult = TestResult.loadFromFile (Settings.resultFolder + d + "/" + fn)
        setResult.appendTestResult (testResult)
      
  @staticmethod
  def printContents ():
    for s in TestResultManager.setResults:
      print (s.name)
      for t in s.testResults:
        print ("  " + t.name)
    
  @staticmethod
  def addSetResult (setResult):
    TestResultManager.setResults.append (TestResultManager.singleRunSet)
    
class SetResult:
  def __init__ (self, name):
    self.name         = name
    self.testResults  = []

  def getResultPath (self):
    return Settings.resultFolder + self.name + "/"
    
  def addTestResult (self, testResult):
    testResult.saveToFile (self.getResultPath ())
    self.appendTestResult (testResult)

  def appendTestResult (self, testResult):
    self.testResults.append (testResult)

  def isSuccess (self):
    for tr in self.testResults:
      if not tr.isSuccess ():
        return False
    return True

class TestResult:
  def __init__ (self, name):
    self.name     = name
    self.criteria = []
    
  def initCriteria (self, criteriaNames):
    for cn in criteriaNames:
      self.criteria.append (Criteria (cn))
    
  def saveToFile (self, directory):
    if (not os.path.isdir (directory)):
      os.makedirs (directory)
    filepath = directory + self.name + ".rslt"
    
    try:
      file = open (filepath,'wb') 
      pickle.dump (self, file)
      file.close()
    except:
      print ("Failed to save " + filepath)

  @staticmethod
  def loadFromFile (filepath):
    try:
      file = open (filepath,'rb') 
    except:
      print ("Failed to load " + filepath + ": " + str (sys.exc_info()[0]))
      return None
      
    try:
      ret = pickle.load (file)
    except:
      print ("Failed to unpickle " + filepath + ": " + str (sys.exc_info()[0]))
      ret = None
      
    file.close()
    return ret
  
  def addEvaluation (self, criteriaName, text, success, time, log):
    criteria = None
    for c in self.criteria:
      if (c.name == criteriaName):
        criteria = c
        break

    if (criteria == None):
      criteria = Criteria (criteriaName)
      self.criteria.append (criteria)
      
    criteria.evaluate (text, success, time, log)

  def isSuccess (self):
    for c in self.criteria:
      if not c.isSuccess():
        return False
    return True

  def log (self, log):
    log.mediumHeading ("Result for " + self.name)

    for c in self.criteria:
      c.printResult (log)

    log.put ("\nTotal test result: " + Log.getSuccessFailed (self.isSuccess ()))

class Criteria:
  def __init__ (self, name):
    self.name = name
    self.evaluations = [];
    self.success   = False;

  def evaluate (self, text, success, time, log):
    self.evaluations.append (CriteriaEval (time, text, success))
    
    log.smallHeading ("Criteria: " + self.name)
    log.put (text + ": " + Log.getSuccessFailed (success) + "\n")
            
  def getResult (self):
    if (not self.isEvaluated ()):
      return "Not evaluated";
      
    return Log.getSuccessFailed (self.isSuccess ())
  
  def isEvaluated (self):
    return len (self.evaluations) != 0
  
  def isSuccess (self):
    if (not self.isEvaluated ()):
      return False;
    
    for e in self.evaluations:
      if (not e.success):
        return False;
    
    return True;

  def printResult (self, log):
    log.put (Log.extend (self.name + ": ", 30, " ") + self.getResult ())
    for e in self.evaluations:
      log.put (Log.extend ("  " + e.text, 30, " ") + Log.getSuccessFailed (e.success) + " (%.1f" % (e.time * 1000) + "ms)")
      
    log.put ("")
      

class CriteriaEval:
  def __init__ (self, time, text, success):
    self.time = time
    self.text = text
    self.success = success;
