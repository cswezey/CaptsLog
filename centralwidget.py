from PyQt4 import QtCore, QtGui
from entrywidget import Entry_Widget
from viewwidget import View_Widget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class CentralWidget(QtGui.QWidget):
    """Set up the central GUI.

    The CentralWidget consist of three main widgets including the
    journal list, journal entry, and journal view.

    """

    def __init__(self, parent):
        """Initialize Central Widget.

        Set up the caller function as reference when
        this class is initiated. Then calls the __CentralWidget
        function and __HorizLayout function.

        """
        super(CentralWidget, self).__init__(parent)
        self.__CentralWidget()
        self.__HorizLayout()

    def __CentralWidget(self):
        """Set up central widget.

        The central widget is given a fixed initial sized and
        is changable according to the window size.

        Args:
            sizePolicy (QSizePolicy) : size policy that defines the initial
                                        size of the central widget and policy
                                        changes of the size.

        """
        self.centralWidget = QtGui.QWidget(self)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

    def __HorizLayout(self):
        """Set up Horizontal Layout.

        This Layout allows all widgets within scales along
        with the window.

        """
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_7.setMargin(11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))

        self.journalTableLayout = QtGui.QHBoxLayout()
        self.journalTableLayout.setMargin(11)
        self.journalTableLayout.setSpacing(6)
        self.journalTableLayout.setObjectName(_fromUtf8("journalTableLayout"))
        self.__JournalList()
        self.journalTableLayout.addWidget(self.journalList)
        self.horizontalLayout_7.addLayout(self.journalTableLayout)

        self.entry = Entry_Widget(self)

        self.view = View_Widget(self)

        self.setLayout(self.horizontalLayout_7)

    def __JournalList(self):
        """Journal List widget."""
        self.journalList = QtGui.QListWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.journalList.sizePolicy().hasHeightForWidth())
        self.journalList.setSizePolicy(sizePolicy)
        self.journalList.setMinimumSize(QtCore.QSize(100, 600))
        self.journalList.setMaximumSize(QtCore.QSize(250, 16777215))
        self.journalList.setObjectName(_fromUtf8("journalList"))

	def initToolbar (self):
			
		#Initializes the functions for the toolbar items
		#The New icon will create a new journal window
		#The Open icon will open the selected journal in the list.
		#The Save icon will save the current opened journal to the journal list
		#The Print icon will open up a PyQt widget to print the contents of Journal Preview
		#The Cut icon will just cut the contents of the QTextEdit widget
		#The Paste icon will just paste the contents of the clipboard to the QTextEdit widget
		#The Help icon will open a browser window with an HTML copy of the Markdown syntax

		self.newAction = QtGui.QAction(QtGui.QIcon("images/filenew.png"), "New", self)
		self.newAction.setStatusTip("Create a new Journal entry.")
		self.newAction.setShortcut("Ctrl + N")
		self.newAction.triggered.connect(self.new)
	
		self.openAction = QtGui.QAction(QtGui.QIcon("images/fileopen.png"), "Open file", self)
		self.openAction.setStatusTip("Open existing journal entry")
		self.openAction.setShortcut("Ctrl + O")
		self.openAction.triggered.connect(self.open)
	
		self.saveAction = QtGui.QAction(QtGui.QIcon("images/filesave.png"), "Save", self)
		self.saveAction.setStatusTip("Save journal entry")
		self.saveAction.setShortcut("Ctrl + S")
		self.saveAction.triggered.connect(self.save)
		
		self.printAction = QtGui.QAction(QtGui.QIcon("images/icon.png"), "Print journal", self)
		self.printAction.setStatusTip("Print journal entry")
		self.printAction.setShortcut("Ctrl + P")
		self.printAction.triggered.connect(self.printHandler)
		
		self.cutAction = QtGui.QAction(QtGui.QIcon("images/editcut.png"), "Cut to clipboard", self)
		self.cutAction.setStatusTip("Delete this text and copy the text to the clipboard")
		self.cutAction.setShortcut("Ctrl + x")
		self.cutAction.triggered.connect(self.text.cut)
		
		self.copyAction = QtGui.QAction(QtGui.QIcon("images/editcopy.png"), "Copy to the clipboard", self)
		self.copyAction.setStatusTip("Copy text to the clipboard")
		self.copyAction.setShortcut("Ctrl + C")
		self.copyAction.triggered.connect(self.text.copy)
		
		self.pasteAction = QtGui.QAction(QtGui.QIcon("images/editpaste.png"), "Paste from clipboard", self)
		self.pasteAction.setStatusTip("Pastes text from the clipboard")
		self.pasteAction.setShortcut("Ctrl + V")
		self.pasteAction.triggered.connect(self.text.paste)
		
		self.undoAction = QtGui.QAction(QtGui.QIcon("images/undo.png"), "Undo last action", self)
		self.undoAction.setStatusTip("Undo last action")
		self.undoAction.setShortcut("Ctrl + Z")
		self.undoAction.triggered.connect(self.text.undo)
		
		self.redoAction = QtGui.QAction(QtGui.QIcon("images/redo.png"), "Redo last action", self)
		self.redoAction.setStatusTip("Redo last action")
		self.redoAction.setShortcut("Ctrl + Y")
		self.redoAction.triggered.connect(self.text.redo)
		
		self.helpAction = QtGui.QAction(QtGui.QIcon("images/help.png"), "Open a browser window with a list of Markdown text and examples", self)
		self.helpAction.setStatusTip("Markdown text examples")
		self.helpAction.setShortcut("Ctrl + H")
		self.helpAction.triggered.connect(self.helpmarkdown)
		
		
		
		#Formats and separates the toolbar menus
		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)
		self.toolbar.addAction(self.printAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.helpAction)
		
		self.addToolBarBreak()
	
	
	def initFormatbar(self):
		
		#Creates a Format menu
		self.formatbar = self.addToolBar("Format")
		
	def initMenubar(self):
		
		menubar = self.menubar()
		
		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")
		
		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.printAction)

		edit.addAction(self.undoAction)
		edit.addAction(self.redoAction)
		edit.addAction(self.cutAction)
		edit.addAction(self.copyAction)
		edit.addAction(self.pasteAction)
		
		view.addAction(self.helpAction)
		
