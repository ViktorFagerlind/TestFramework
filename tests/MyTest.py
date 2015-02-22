from Log  import Log
from Test import Test

class MyTest (Test):
  def __init__ (self):
    Test.__init__(self, "My Test")
           
  def runSequence (self):
    self.initCriteria (["Check file",
                        "Check constant",
                        "Check all files present",
                        "W is correct",
                        "Power is correct"])
  
    Log.put ("Simple check")

    Test.printSubstep ("File checking")
    self.check ("Check file", "Correct formatting", True)
    self.check ("Check file", "Correct encoding", True)
    self.check ("Check file", "Correct contents", True)

    Test.printSubstep ("Value checking")
    self.check ("Check constant", "C = W^2", False);

    Test.printSubstep ("Misc checking")
    self.check ("Check all files present", "test directory", True);

    val = 0
    #....
    val = 120
    self.checkEqual ("Power is correct", "W", val, 120)
        


