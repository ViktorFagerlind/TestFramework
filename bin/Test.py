import datetime
import time

from Log 		    import Log
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
    self.ongoingResult.addEvaluation (criteriaName, text, success, time.time () - self.startTime)

  def printStart (self):
    Log.largeHeading (self.name)
    Log.put ("\n")

  @staticmethod
  def printSubstep (name):
    Log.put ("\n")
    Log.mediumHeading (name)

  def run (self):
    self.startTime = time.time ()
    timeName = (self.name + " - " + str (datetime.datetime.now())).replace (':','.')

    Log.startFileLogging (timeName)
    self.ongoingResult = TestResult (timeName)
    self.printStart ()
    self.runSequence ()
    
    Log.mediumHeading (self.name + " done!")

    self.ongoingResult.saveToFile ()
    self.ongoingResult.log ()
    
    Log.stopFileLogging ()


