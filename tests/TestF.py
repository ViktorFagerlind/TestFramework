from Log  import Log
from Test import Test

class TestF (Test):
  def __init__ (self):
    Test.__init__(self, "Test F")
           
  def runSequence (self):
    Test.printSubstep ("Sub test 1")
        


