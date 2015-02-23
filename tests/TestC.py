from Log  import Log
from Test import Test

class TestC (Test):
  def __init__ (self):
    Test.__init__(self, "Test C")
           
  def runSequence (self):
    Test.printSubstep ("Sub test 1")
        


