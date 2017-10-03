import sys
sys.path.insert(0, "..\\bin")

from Test import Test

import logging

class TestB (Test):
  def __init__ (self, instanceName="Default"):
    Test.__init__(self, "Test B", instanceName)
           
  def runSequence (self):
    logging.info('Started')
    logging.warning('Running...')
    logging.info('Stopped')


if __name__ == '__main__':
  test = TestB()
  logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
  
  fh = logging.FileHandler(filename=test.instanceName + '.log')
  fh.setFormatter (logging.Formatter ('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
  logging.getLogger().addHandler(fh)
  
  test.runSequence()
