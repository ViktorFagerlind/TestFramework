import time
import sys

from TestManager  import TestConfiguration
from Logging      import Log, LogManager, Settings, StreamToLog
from Results      import TestResult


class Test:
  def __init__ (self, name, instanceName):
    self.name         = name
    self.instanceName = instanceName

  def fullName (self):
   return self.name + " (" + self.instanceName + ")"

  def getFloatParameter (self, name, default=0):
    valueString = TestConfiguration.getValueString (self.name, self.instanceName, name)
    if (valueString == None):
      return float (default)
    return float (valueString)

  def getIntParameter (self, name, default=0):
    valueString = TestConfiguration.getValueString (self.name, self.instanceName, name)
    if (valueString == None):
      return int (default)
    return int (valueString)

  def getLongParameter (self, name, default=0):
    valueString = TestConfiguration.getValueString (self.name, self.instanceName, name)
    if (valueString == None):
      return long (default)
    return long (valueString)

  def checkEqual (self, criteriaName, variableName, actualValue, expectedValue):
    self.check (criteriaName, variableName + "=" + str(expectedValue), actualValue == expectedValue)
      
  def initCriteria (self, criteriaNames):
    self.ongoingResult.initCriteria (criteriaNames)
  
  def check (self, criteriaName, text, success):
    self.ongoingResult.addEvaluation (criteriaName, text, success, time.time () - self.startTime, self.log)

  def printStart (self):
    self.log.largeHeading (self.timeName)
    self.log.newline ()

  def printSubstep (self, name):
    self.log.newline ()
    self.log.mediumHeading (name)

  def run (self, setResult):
    Log.mainLog.put ("Starting test: " + self.fullName ())

    self.startTime = time.time ()
    self.timeName = self.fullName () + " - " + Settings.getNowString ()

    self.log = LogManager.addLog (self.fullName (), setResult.getResultPath (), self.timeName)
    self.ongoingResult = TestResult (self.timeName, setResult.getResultPath ())

    normalStdout = sys.stdout
    normalStderr = sys.stderr
    sys.stdout   = StreamToLog(self.log, False)
    sys.stderr   = StreamToLog(self.log, True)

    print ("1 Stdout")
    print ("1 Stderr", file=sys.stderr)

    self.printStart ()
    self.runSequence ()

    sys.stdout = normalStdout
    sys.stderr = normalStderr

    print ("2 Stdout")
    print ("2 Stderr", file=sys.stderr)

    self.log.mediumHeading (self.name + " done!")
    self.ongoingResult.log (self.log)

    setResult.addTestResult (self.ongoingResult)
