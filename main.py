#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 Roark <roark@roark-Satellite-A665>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#Import the libraries needed for PyQt
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

import markdown


class Main(QtGui.QMainWindow):
	
	#Initialize the main window of the application 
	def __init__(self, parent = None):
		QtGui.QMainWindow.__init__(self, parent)
		
		self.filename = ""
		
		self.initUI()
	
	def initToolbar(self):
	
	#Initializes the toolbar menu options for New, Open, and Save functions
	#Also sets their descriptions, shortcuts, and actions
	
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
	
		#self.toolbar = self.addToolBar("Options")
		
		self.printAction = QtGui.QAction(QtGui.QIcon("images/fileopen.png"), "Print journal", self)
		self.printAction.setStatusTip("Print journal entry")
		self.printAction.setShortcut("Ctrl + P")
		self.printAction.triggered.connect(self.printHandler)
		
		self.previewAction = QtGui.QAction(QtGui.QIcon("images/editcopy.png"), "Journal preview", self)
		self.previewAction.setStatusTip("Preview journal before printing")
		self.previewAction.setShortcut("Ctrl + Shift + P")
		self.previewAction.triggered.connect(self.preview)
		
		self.cutAction = QtGui.QAction(QtGui.QIcon("images/editcut.png"), "Cut to clipboard", self)
		self.cutAction.setStatusTip("Delete this text and copy the text to the clipboard")
		self.cutAction.setShortcut("Ctrl + x")
		self.cutAction.triggered.connect(self.text.cut)
		
		self.copyAction = QtGui.QAction(QtGui.QIcon("images/editcopy.png"), "Copy to the clipboard", self)
		self.copyAction.setStatusTip("Copy text to the clipboard")
		self.copyAction.setShortcut("Ctrl + C")
		self.copyAction.triggered.connect(self.text.copy)
		
		self.pasteAction = QtGui.QAction(QtGui.QIcon("images/editpase.png"), "Paste from clipboard", self)
		self.pasteAction.setStatusTip("Pastes text from the clipboard")
		self.pasteAction.setShortcut("Ctrl + V")
		self.pasteAction.triggered.connect(self.text.paste)
		
		self.undoAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Undo last action", self)
		self.undoAction.setStatusTip("Undo last action")
		self.undoAction.setShortcut("Ctrl + Z")
		self.undoAction.triggered.connect(self.text.undo)
		
		self.redoAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Redo last action", self)
		self.redoAction.setStatusTip("Redo last action")
		self.redoAction.setShortcut("Ctrl + Y")
		self.redoAction.triggered.connect(self.text.undo)
		
		bulletAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Insert bulleted list", self)
		bulletAction.setStatusTip("Insert bullet list")
		bulletAction.setShortcut("Ctrl + Shift + B")
		bulletAction.triggered.connect(self.bulletList)
		
		numberedAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Insert numbered list", self)
		numberedAction.setStatusTip("Insert numbered list")
		numberedAction.setShortcut("Ctrl + Shift + L")
		numberedAction.triggered.connect(self.numberList)
		
		headerAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Insert title head", self)
		headerAction.setStatusTip("Insert title headers")
		headerAction.setShortcut("Ctrl + Shift + H")
		headerAction.triggered.connect(self.header)
		
		emphasisAction = QtGui.QAction(QtGui.QIcon("images/editdelete.png"), "Put emphasis on the selected word", self)
		emphasisAction.setStatusTip("Put emphasis on the selected word")
		emphasisAction.setShortcut("Ctrl + Shift + E")
		emphasisAction.triggered.connect(self.emphasis)
		
		self.toolbar = self.addToolBar("Options")
	
		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)
	
	#Formats and separates the toolbar menus
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)
		
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)
		self.toolbar.addAction(headerAction)
		self.toolbar.addAction(emphasisAction)
		
		
		self.addToolBarBreak()
		
	def initFormatbar(self):
	
		#Creates a Format menu
		self.formatbar = self.addToolBar("Format")
		
	def initMenubar(self):
	
		menubar = self.menuBar()
	
		#Creates objects for the toolbar menus
		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")
		
		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)
		
		edit.addAction(self.undoAction)
		edit.addAction(self.redoAction)
		edit.addAction(self.cutAction)
		edit.addAction(self.copyAction)
		edit.addAction(self.pasteAction)

	def initUI(self):
		
		self.text = QtGui.QTextEdit(self)
		
		self.initToolbar()
		self.initFormatbar()
		self.initMenubar()
		
		self.text.setTabStopWidth(33)
		self.setCentralWidget(self.text)
		#self.setCentralWidget(self.text)
		
		self.statusbar = self.statusBar()
		self.text.cursorPositionChanged.connect(self.cursorPosition)
		
		self.setGeometry(100, 100, 1030, 800)
		self.setWindowTitle("CaptsLog")
		self.setWindowIcon(QtGui.QIcon("/images/icon.png"))
		
	def new(self):

		spawn = Main(self)
		spawn.show()

	def open(self):

		# Get filename and show only .markdown files
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.markdown)")

		if self.filename:
			with open(self.filename,"rt") as file:
				self.text.setText(file.read())

	def save(self):

        # Only open dialog if there is no filename yet
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
	#	if not self.filename.endswith(".markdown"):
	#		self.filename += ".markdown"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
		with open(self.filename,"wt") as file:
			file.write(self.text.toHtml())

	def preview(self):

        # Open preview dialog
		preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
		preview.paintRequested.connect(lambda p: self.text.print_(p))

		preview.exec_()

	def printHandler(self):

        # Open printing dialog
		dialog = QtGui.QPrintDialog()

		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.text.document().print_(dialog.printer())


	def cursorPosition(self):

		cursor = self.text.textCursor()

        # Mortals like 1-indexed things
		line = cursor.blockNumber() + 1
		col = cursor.columnNumber()

		self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

	def bulletList(self):

		cursor = self.text.textCursor()
		cursor.insertText(markdown.markdown('*'))
        # Insert bulleted list	
		#cursor.insertList(QtGui.QTextListFormat.ListDisc)

	def numberList(self):

		cursor = self.text.textCursor()

        # Insert list with numbers
		cursor.insertList(QtGui.QTextListFormat.ListDecimal)

	def header (self):
		
		cursor = self.text.textCursor()
		cursor.insertText(markdown.markdown('#'))
		
	def emphasis (self):
		
		cursor = self.text.textCursor()
		cursor.insertText(markdown.markdown('#'))
		""" Function doc """
class Preview(QtGui.QMainWindow):
	
	def __init__(prev, parent = None):
		
		QtGui.QMainWindow.__init__(prev, parent)
		
		prev.initUI()
		
		def initUI(prev):
			prev.setGeometry(100, 100, 1030, 800)
			prev.setWindowTitle("Journal Preview")
			
	
			""" Function doc """
			
		""" Function doc """
		
	""" Function doc """
			
def main():

	app = QtGui.QApplication(sys.argv)

	main = Main()
	main.show()

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
