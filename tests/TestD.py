from Log  import Log
from Test import Test

class TestD (Test):
  def __init__ (self):
    Test.__init__(self, "Test D")
           
  def runSequence (self):
    Test.printSubstep ("Sub test 1")
        


