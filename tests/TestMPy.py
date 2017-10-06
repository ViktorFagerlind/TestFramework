import io
import sys

sys.path.insert(0, "C:\\development\\Mine\\TestFramework\\bin")
from Logging    import Log
from Test       import Test

import logging

sys.path.insert(0, "C:\\Utilities\\python-tem")
import test6

class TestMPy (Test):
  def __init__ (self, instanceName):
    Test.__init__(self, "Test micro-python", instanceName)
           
  def runSequence (self):
    f = self.getFloatParameter ("Force")
  
    self.printSubstep ("Running test6")
    test6.run()
    
    print ("This is a print")
    
    logging.basicConfig(level=logging.INFO)
    logging.info ("This is info logging")
    self.log.logger.info ("This is info logging")

if __name__ == '__main__':
  t = TestMPy("Default")
  t.runStandalone ()
  