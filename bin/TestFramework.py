import sys
from PySide import QtGui
from QtWidget import Ui_Widget

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_Widget()
    self.ui.setupUi(self)
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())