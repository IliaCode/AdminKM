# coding: utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from main_gui import *
import time
import pyautogui
#Create Application
app = QtWidgets.QApplication(sys.argv)

#Initing All
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
Form.setWindowIcon(QIcon('cursor.png'))

#Hook logic
#-----------------------------------------------------------------------------------------------------------------
#main scenary list
todo = []

aviable_buttons_list = [' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[',  ']', '^', '_',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',  '}', 
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

class ListWid():
	'''Class for Admininstrating QListWidget'''	
	def move_mouse(self):
		#Method for admining 'move mouse' key
		try:
			#Code for moving mouse
			x = int(ui.corx.text())
			y = int(ui.cory.text())
			todo.append('pyautogui.moveTo({0},{1})'.format(x,y))
			print(todo)
			ui.listwidget.addItem('Moving Mouse to: X:{0}, Y:{1}'.format(x,y))
		except ValueError:
			pyautogui.alert('Put coordinats X and Y (only numbers)')
	
	def keypress(self):
		'''Class for Admining '''
		try:
			#Code for detect key
			key = str(ui.click1.text())
			if key == '':
				pyautogui.alert(text='put one key from list:{}'.format(aviable_buttons_list), title='Key Error')
			else:
				todo.append("pyautogui.press('{}')".format(key))
				print(todo)
				ui.listwidget.addItem('Pressing: {0}'.format(key))
		except:
			pyautogui.alert()

	def sleep(self):
		try:
			timesleep = int(ui.tine.text())
			todo.append('time.sleep({})'.format(timesleep))
			print(todo)
			ui.listwidget.addItem('Sleeping: {0} seconds'.format(timesleep))
		except:
			pyautogui.alert('Put interval of seconds (only numbers)')

	def hotkey(self):
		try:
			key1 = ui.hok1.text()
			key2 = ui.hok2.text()
			if key1 == '':
				pyautogui.alert('Please put 2 hot keys')
			elif key2 == '':
				pyautogui.alert('Please put 2 hot keys')
			else:
				todo.append("pyautogui.hotkey('{0}','{1}')".format(key1,key2))
				print(todo)
				ui.listwidget.addItem('Pressing {0} and {1}'.format(key1, key2))
		except:
			pyautogui.alert('Please put hot keys')

	def clear(self):
		'''Cleans All items in LIST'''
		ui.listwidget.clear()
		list_bullet = len(todo)
		todo.clear()



class other_func():
	'''Class for admining events after pushing start button and other buttons'''
	def after_push(self):
		#close main window for work
		Form.showMinimized()
		#number of operations
		number_op = int(ui.listwidget.count())
		for i in range(number_op):
			eval(todo[i])



ui.clear.clicked.connect(ListWid.clear)
ui.pushButton.clicked.connect(other_func.after_push)
ui.slep.clicked.connect(ListWid.sleep)
ui.click.clicked.connect(ListWid.keypress)
ui.movem.clicked.connect(ListWid.move_mouse)
ui.pushButton_2.clicked.connect(ListWid.hotkey)


#Main Loop
sys.exit(app.exec_())
