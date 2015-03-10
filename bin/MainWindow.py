# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Mar 10 21:58:21 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 837)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTests = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTests.sizePolicy().hasHeightForWidth())
        self.labelTests.setSizePolicy(sizePolicy)
        self.labelTests.setObjectName("labelTests")
        self.verticalLayout.addWidget(self.labelTests)
        self.splitter = QtGui.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidgetTest = QtGui.QTabWidget(self.splitter)
        self.tabWidgetTest.setObjectName("tabWidgetTest")
        self.TreeViewResults = QtGui.QTreeView(self.splitter)
        self.TreeViewResults.setObjectName("TreeViewResults")
        self.verticalLayout.addWidget(self.splitter)
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
        self.verticalLayout_2.addWidget(self.tabWidgetLog)
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startSetButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../data/icons/Play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startSetButton.setIcon(icon)
        self.startSetButton.setObjectName("startSetButton")
        self.horizontalLayout.addWidget(self.startSetButton)
        self.startTestButton = QtGui.QPushButton(self.centralwidget)
        self.startTestButton.setIcon(icon)
        self.startTestButton.setObjectName("startTestButton")
        self.horizontalLayout.addWidget(self.startTestButton)
        self.abortButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../data/icons/Cancel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abortButton.setIcon(icon1)
        self.abortButton.setObjectName("abortButton")
        self.horizontalLayout.addWidget(self.abortButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
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
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionStartTest = QtGui.QAction(MainWindow)
        self.actionStartTest.setIcon(icon)
        self.actionStartTest.setObjectName("actionStartTest")
        self.actionAbort = QtGui.QAction(MainWindow)
        self.actionAbort.setIcon(icon1)
        self.actionAbort.setObjectName("actionAbort")
        self.actionStartSet = QtGui.QAction(MainWindow)
        self.actionStartSet.setIcon(icon)
        self.actionStartSet.setObjectName("actionStartSet")
        self.menuFile.addAction(self.actionQuit)
        self.menuTest.addAction(self.actionStartSet)
        self.menuTest.addAction(self.actionStartTest)
        self.menuTest.addAction(self.actionAbort)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.toolBar.addAction(self.actionStartSet)
        self.toolBar.addAction(self.actionStartTest)
        self.toolBar.addAction(self.actionAbort)

        self.retranslateUi(MainWindow)
        self.tabWidgetTest.setCurrentIndex(-1)
        self.tabWidgetLog.setCurrentIndex(-1)
        QtCore.QObject.connect(self.startSetButton, QtCore.SIGNAL("clicked()"), self.actionStartSet.trigger)
        QtCore.QObject.connect(self.startTestButton, QtCore.SIGNAL("clicked()"), self.actionStartTest.trigger)
        QtCore.QObject.connect(self.abortButton, QtCore.SIGNAL("clicked()"), self.actionAbort.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTests.setText(QtGui.QApplication.translate("MainWindow", "Test Collections", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLog.setText(QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.startSetButton.setText(QtGui.QApplication.translate("MainWindow", "Start Test Set", None, QtGui.QApplication.UnicodeUTF8))
        self.startTestButton.setText(QtGui.QApplication.translate("MainWindow", "Start Test", None, QtGui.QApplication.UnicodeUTF8))
        self.abortButton.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartTest.setText(QtGui.QApplication.translate("MainWindow", "Start Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartTest.setToolTip(QtGui.QApplication.translate("MainWindow", "Start Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbort.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartSet.setText(QtGui.QApplication.translate("MainWindow", "Start Test Set", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartSet.setToolTip(QtGui.QApplication.translate("MainWindow", "Start Test", None, QtGui.QApplication.UnicodeUTF8))

