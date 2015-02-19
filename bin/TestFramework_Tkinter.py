from Tkinter import *

class Application(Frame):
  def run(self):
    print "hi there, everyone!"

  def createWidgets(self, master):
    top=self.winfo_toplevel ()
    top.rowconfigure (0, weight=1)
    top.columnconfigure (0, weight=1)
    
    self.rowconfigure (0, weight=1)
    self.columnconfigure (1, weight=1)  

    testFrame = LabelFrame (self, text='Tests', padx=5, pady=5)
    testFrame.grid (row=0, column=0, rowspan=2, sticky=N+S+E+W)
    testFrame.rowconfigure (0, weight=1)
  
    testsBox = Listbox (self)
    testsBox.insert(END, "a list entry")
    for item in ["one", "two", "three", "four"]:
        testsBox.insert(END, item)
    testsBox.grid (in_=testFrame, row=0, sticky=N+S+E+W)
    
    logFrame = LabelFrame (self, text='Log', padx=5, pady=5)
    logFrame.grid (row=0, column=1, rowspan=2, sticky=N+S+E+W)
    logFrame.rowconfigure (0, weight=1)
    logFrame.columnconfigure (0, weight=1)
    
    logBox = Listbox (self)
    logBox.grid (in_=logFrame, sticky=N+S+E+W)
    
    commandFrame = LabelFrame (self, text='Commands', padx=5, pady=5)
    commandFrame.grid (row=2, columnspan=2, sticky=E+W)
    commandFrame.columnconfigure (0, weight=1)
    commandFrame.columnconfigure (1, weight=1)
    commandFrame.columnconfigure (2, weight=1)
  
    self.QUIT = Button (self, text="QUIT", fg="red", command = self.quit)
    self.QUIT.grid (in_=commandFrame, row=0, column=0, sticky=W)

    self.run = Button (self, text="Run", command = self.run)
    self.run.grid (in_=commandFrame, row=0, column=1, sticky=W)
    
    self.abort = Button (self, text="Abort", command = self.run)
    self.abort.grid (in_=commandFrame, row=0, column=2, sticky=W)
    
  def __init__(self, master=None):
    Frame.__init__(self, master, padx=5, pady=5)
    self.grid(sticky=W+E+N+S)
    self.createWidgets(master)

root = Tk ()
app = Application (master=root)
app.mainloop ()
root.destroy ()