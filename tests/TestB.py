from Log  import Log
from Test import Test

class TestB (Test):
  def __init__ (self):
    Test.__init__(self, "Test B")
           
  def runSequence (self):
    self.printSubstep ("Sub test 1")
        


