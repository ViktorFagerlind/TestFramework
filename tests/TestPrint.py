import io
import sys

sys.path.insert(0, "D:\\Libraries\\Programming\\Python\\TestFramework\\bin")
from Logging    import Log
from Test       import Test

import logging

class TestPrint (Test):
  def __init__ (self, instanceName):
    Test.__init__(self, "Test printing", instanceName)
           
  def runSequence (self):
    f = self.getFloatParameter ("Force")
  
    self.printSubstep ("Running Print test")

    print ("Printing")
    self.log.put     ('Put logging')
    logging.debug    ('Debug logging')
    logging.info     ('Info logging')
    logging.warning  ('Warning logging')
    logging.error    ('Error logging')
    logging.critical ('Critical logging')


if __name__ == '__main__':
  t = TestPrint("Default")
  t.runStandalone ()
  