import datetime
import time

from TestManager  import TestConfiguration
from Log 		      import Log, LogManager
from TestResult   import TestResult

class Test:
  def __init__ (self, name, instanceName):
    self.name         = name
    self.instanceName = instanceName

  def fullName (self):
   return self.name + " (" + self.instanceName + ")"

  def getFloatParameter (self, name, default):
    valueString = TestConfiguration.getValueString (self.name, self.instanceName, name)
    if (valueString == None):
      return float (default)
    return float (valueString)

  def checkEqual (self, criteriaName, variableName, actualValue, expectedValue):
    self.check (criteriaName, variableName + "=" + str(expectedValue), actualValue == expectedValue)
      
  def initCriteria (self, criteriaNames):
    self.ongoingResult.initCriteria (criteriaNames)
  
  def check (self, criteriaName, text, success):
    self.ongoingResult.addEvaluation (criteriaName, text, success, time.time () - self.startTime, self.log)

  def printStart (self):
    self.log.largeHeading (self.timeName)
    self.log.put ("")

  def printSubstep (self, name):
    self.log.put ("\n")
    self.log.mediumHeading (name)

  def run (self):
    self.startTime = time.time ()
    self.timeName = (self.fullName () + " - " + str (datetime.datetime.now())).replace (':','.')

    self.log = LogManager.addLog (self.fullName ())
    self.log.startFileLogging (self.timeName)
    self.ongoingResult = TestResult (self.timeName)
    self.printStart ()
    self.runSequence ()
    
    self.log.mediumHeading (self.name + " done!")

    self.ongoingResult.saveToFile ()
    self.ongoingResult.log (self.log)
    
    self.log.stopFileLogging ()


