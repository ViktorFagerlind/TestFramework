# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat Feb 28 16:48:51 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_2 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTests = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTests.sizePolicy().hasHeightForWidth())
        self.labelTests.setSizePolicy(sizePolicy)
        self.labelTests.setObjectName("labelTests")
        self.verticalLayout.addWidget(self.labelTests)
        self.tabWidgetTest = QtGui.QTabWidget(self.layoutWidget_2)
        self.tabWidgetTest.setObjectName("tabWidgetTest")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listViewTests = QtGui.QListView(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewTests.sizePolicy().hasHeightForWidth())
        self.listViewTests.setSizePolicy(sizePolicy)
        self.listViewTests.setObjectName("listViewTests")
        self.horizontalLayout_2.addWidget(self.listViewTests)
        self.tabWidgetTest.addTab(self.tab_1, "")
        self.verticalLayout.addWidget(self.tabWidgetTest)
        self.layoutWidget_3 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelLog = QtGui.QLabel(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLog.sizePolicy().hasHeightForWidth())
        self.labelLog.setSizePolicy(sizePolicy)
        self.labelLog.setObjectName("labelLog")
        self.verticalLayout_2.addWidget(self.labelLog)
        self.tabWidgetLog = QtGui.QTabWidget(self.layoutWidget_3)
        self.tabWidgetLog.setObjectName("tabWidgetLog")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listViewLog = QtGui.QListView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewLog.sizePolicy().hasHeightForWidth())
        self.listViewLog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.listViewLog.setFont(font)
        self.listViewLog.setMovement(QtGui.QListView.Free)
        self.listViewLog.setObjectName("listViewLog")
        self.verticalLayout_4.addWidget(self.listViewLog)
        self.tabWidgetLog.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidgetLog)
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.abortButton = QtGui.QPushButton(self.centralwidget)
        self.abortButton.setObjectName("abortButton")
        self.horizontalLayout.addWidget(self.abortButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionAbort = QtGui.QAction(MainWindow)
        self.actionAbort.setObjectName("actionAbort")
        self.menuFile.addAction(self.actionQuit)
        self.menuTest.addAction(self.actionStart)
        self.menuTest.addAction(self.actionAbort)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionAbort)

        self.retranslateUi(MainWindow)
        self.tabWidgetTest.setCurrentIndex(0)
        self.tabWidgetLog.setCurrentIndex(0)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("clicked()"), self.actionQuit.trigger)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL("clicked()"), self.actionStart.trigger)
        QtCore.QObject.connect(self.abortButton, QtCore.SIGNAL("clicked()"), self.actionAbort.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTests.setText(QtGui.QApplication.translate("MainWindow", "Test Collections", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetTest.setTabText(self.tabWidgetTest.indexOf(self.tab_1), QtGui.QApplication.translate("MainWindow", "All Tests", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLog.setText(QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLog.setTabText(self.tabWidgetLog.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Main Log", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbort.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))

