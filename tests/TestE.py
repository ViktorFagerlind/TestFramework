from Log  import Log
from Test import Test

class TestE (Test):
  def __init__ (self):
    Test.__init__(self, "Test E")
           
  def runSequence (self):
    Test.printSubstep ("Sub test 1")
        


