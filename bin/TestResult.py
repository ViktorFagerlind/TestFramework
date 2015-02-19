import pickle
import datetime
import time

from Log import Log
from Log import Settings


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
  
  def addEvaluation (self, criteriaName, text, success, time):
    criteria = None
    for c in self.criteria:
      if (c.name == criteriaName):
        criteria = c
        break

    if (criteria == None):
      criteria = Criteria (criteriaName)
      self.criteria.append (criteria)
      
    criteria.evaluate (text, success, time)

  def log (self):
    Log.mediumHeading ("Result for " + self.name)

    allSuccess = True;
    for c in self.criteria:
        c.printResult ()
        if not c.isSuccess():
            allSuccess = False    
    
    Log.put ("\nTotal test result: " + Log.getSuccessFailed (allSuccess))

class Criteria:
  def __init__ (self, name):
    self.name = name
    self.evaluations = [];
    self.success   = False;

  def evaluate (self, text, success, time):
    self.evaluations.append (CriteriaEval (time, text, success))
    
    Log.smallHeading ("Criteria: " + self.name)
    Log.put (text + ": " + Log.getSuccessFailed (success) + "\n")
            
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

  def printResult (self):
    Log.put (Log.extend (self.name + ": ", 30, " ") + self.getResult ())
    for e in self.evaluations:
      Log.put (Log.extend ("  " + e.text, 30, " ") + Log.getSuccessFailed (e.success) + " (%.1f" % (e.time * 1000) + "ms)")
      
    Log.put ("")
      

class CriteriaEval:
  def __init__ (self, time, text, success):
    self.time = time
    self.text = text
    self.success = success;
  
