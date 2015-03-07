from Log  import Log
from Test import Test

class TestA (Test):
  def __init__ (self, instanceName):
    Test.__init__(self, "Test A", instanceName)
           
  def runSequence (self):
    self.initCriteria (["Check file",
                        "Check constant",
                        "Check all files present",
                        "W is correct",
                        "Power is correct"])
  
    self.log.put ("Simple check")

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
        


