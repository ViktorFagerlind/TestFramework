import pickle
import datetime
import time

from Log import Log
from Log import Settings

class TestManager:
  setResults = []

#  def setup ():
#    setResults.append ()


class SetResult:
  def __init__ (self, name):
    self.name         = name
    self.testResults  = []

  def addTestResult (self, testResult):
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
    
  def saveToFile (self):
    filepath = Settings.resultFolder + self.name + ".rslt"
    try:
      file = open (filepath,'w') 
      pickle.dump (self, file)
      file.close()
    except:
      print ("Failed to save " + filepath)

  @staticmethod
  def loadFromFile (filepath):
    try:
      file = open (filepath,'r') 
    except:
      print ("Failed to load " + filepath)
      
    return pickle.load (file)
  
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
  
