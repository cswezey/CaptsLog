#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  toolbar.py
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
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from DBHandler import DBHandlerClass

from PyQt4.QtWebKit import QWebView


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

class Toolbars(QtGui.QWidget):
	
	"""
	Defines the various functions for the toolbar that aren't already
	built into PyQt

	"""
	
	def new(self):
		
		self.newAction = QtGui.QAction(MainWindow)
		self.newAction.setObjectName(_fromUtf8("newAction"))
	
	def open(self):
		
		#Get filename and show only .markdown files
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.markdown)")

		if self.filename:
			with open(self.filename,"rt") as file:
				self.text.setText(file.read())
				
	def save(self):

        # Only open dialog if there is no filename yet
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
			
	def printHandler(self):

        # Open printing dialog
		dialog = QtGui.QPrintDialog()

		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.text.document().print_(dialog.printer())
		
	def help(self):
		#Just opens an HTML markdown guide from github.
		view = Browser()
		view.load(QUrl('www.github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet'))
		
		
