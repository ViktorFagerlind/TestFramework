import logging

from Logging  import Log
from Test     import Test

class TestA (Test):
  def __init__ (self, instanceName):
    Test.__init__(self, "Test A", instanceName)
           
  def runSequence (self):
    # Optional initialisation if criteria in order to ensure that they are all checked during the test
    self.initCriteria (["Check file",
                        "Check constant",
                        "Check all files present",
                        "W is correct",
                        "Power is correct"])
  
    self.logger.info ("Simple check")

    # Get input parameter values
    f = self.getFloatParameter ("Force")
    s = self.getFloatParameter ("Speed")
    a = self.getFloatParameter ("Acceleration")

    self.logger.info ("Force: " + str (f))
    self.logger.info ("Speed: " + str (s))
    self.logger.info ("Acceleration: " + str (a))
    self.logger.info ("Sum: " + str (f + s + a))
    self.log.newline ()

    # Read non existent parameter with default value
    falseName = self.getFloatParameter ("What!?", -10)
    self.logger.info ("Default value: " + str (falseName))

    self.printSubstep ("File checking")
    self.check ("Check file", "Correct formatting", True)
    self.check ("Check file", "Correct encoding", True)
    self.check ("Check file", "Correct contents", True)

    self.printSubstep ("Value checking")
    self.check ("Check constant", "C = W^2", False);

    self.printSubstep ("Misc checking")
    self.check ("Check all files present", "test directory", True);

    val = 0
    #....
    val = 120
    self.checkEqual ("Power is correct", "W", val, 120)


