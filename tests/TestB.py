import sys
sys.path.insert(0, "..\\bin")

from Test import Test

import logging

class TestB (Test):
  def __init__ (self, instanceName="Default"):
    Test.__init__(self, "Test B", instanceName)
           
  def runSequence (self):
    self.log.info ('Started')
    self.log.info ('Running...')
    self.log.info ('Stopped')


if __name__ == '__main__':
  t = TestB("Default")
  t.runStandalone ()
