import io
import sys

from Logging    import Log
from Test       import Test

sys.path.insert(0, "C:\\Utilities\\python-tem")
import test6

class TestMPy (Test):
  def __init__ (self, instanceName):
    Test.__init__(self, "Test micro-python", instanceName)
           
  def runSequence (self):
    f = self.getFloatParameter ("Force")
  
    self.printSubstep ("Running test6")
    test6.run()
