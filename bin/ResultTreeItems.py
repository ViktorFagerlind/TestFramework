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
    return 1

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

  def Data(self):
    return "Test Results"
    
  def IsSuccess(self):
    return True 


class NormalTreeItem(BaseTreeItem):
  def __init__(self, parent, name, isSuccess):
    super(NormalTreeItem, self).__init__(parent)
    self.name = name
    self.isSuccess = isSuccess

  def Data(self):
    return self.name

  def IsSuccess(self):
    return self.isSuccess
