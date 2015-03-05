import datetime
import time

from Log 		    import Log, LogManager
from TestResult import TestResult
from TestResult import Criteria

#class TestSet:

class Test:
  def __init__ (self, name):
    self.name     = name

  def checkEqual (self, criteriaName, variableName, actualValue, expectedValue):
    self.check (criteriaName, variableName + "=" + str(expectedValue), actualValue == expectedValue)
      
  def initCriteria (self, criteriaNames):
    self.ongoingResult.initCriteria (criteriaNames)
  
  def check (self, criteriaName, text, success):
    self.ongoingResult.addEvaluation (criteriaName, text, success, time.time () - self.startTime, self.log)

  def printStart (self):
    self.log.largeHeading (self.name)
    self.log.put ("\n")

  def printSubstep (self, name):
    self.log.put ("\n")
    self.log.mediumHeading (name)

  def run (self):
    self.startTime = time.time ()
    timeName = (self.name + " - " + str (datetime.datetime.now())).replace (':','.')

    self.log = LogManager.addLog (self.name)
    self.log.startFileLogging (timeName)
    self.ongoingResult = TestResult (timeName)
    self.printStart ()
    self.runSequence ()
    
    self.log.mediumHeading (self.name + " done!")

    self.ongoingResult.saveToFile ()
    self.ongoingResult.log (self.log)
    
    self.log.stopFileLogging ()


