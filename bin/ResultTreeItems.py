class BaseTreeItem (object):
  def __init__(self, inParentItem):
    self.parent = inParentItem
    self.children = []

  def AddChild(self, inChild):
    self.children.append(inChild)

  def GetChildCount(self):
    return len(self.children)

  def GetChild(self, row):
    return self.children[row]

  def GetParent(self):
    return self.parent

  def ColumnCount(self):
    raise Exception("Column Count Not Specified!!")

  def Data(self):
    raise Exception("Data gather method not implemented!")

  def IsSuccess(self):
    raise Exception("Data gather method not implemented!")

  def Parent(self):
    return self.parent

  def Row(self):
    if self.parent:
      return self.parent.children.index(self)
    return 0

class RootTreeItem(BaseTreeItem):
  def __init__(self):
    super(RootTreeItem, self).__init__(None)

  def ColumnCount(self):
    return 1

  def Data(self):
    return "Test Results"
    
  def IsSuccess(self):
    return True 


class TestResultTreeItem(BaseTreeItem):
  def __init__(self, parent, testResult):
    super(TestResultTreeItem, self).__init__(parent)
    self.testResult = testResult

  def ColumnCount(self):
    return 1

  def Data(self):
    return self.testResult.name

  def IsSuccess(self):
    return self.testResult.isSuccess ()

class CriteriaTreeItem(BaseTreeItem):
  def __init__(self, parent, criteria):
    super(CriteriaTreeItem, self).__init__(parent)
    self.criteria = criteria

  def ColumnCount(self):
    return 1

  def Data(self):
    return self.criteria.name

  def IsSuccess(self):
    return self.criteria.isSuccess ()

