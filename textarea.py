# -*- coding: utf-8 -*-

from   tkinter import *
from   tkinter import ttk
from   tkinter.messagebox import showinfo
import tkinter.filedialog as fd
import re


import logs # import logWrite
import os
import shutil
import subprocess
# import sys
import _thread
	

finalCatalog 	= ''
inputExtension 	= '.pdf'
availableExtensions = ['.jpg', '.png', '.cfe', '.cfu', '.epf']
except_extension = ['.cfl', '.dat']
listMD5 		= []
dMode			= True


def txtQuit(q):
	if q == 'q':
		print('EXIT PROGRAMM')
		quit()
		

def txtDebug(val = ''):
	
	if len(val) > 0 and val.upper() == 'Y':
		print('Install mode: --> DEBUG PROGRAMM')
		return True
	return False





# Widget.__init__(self, master, 'frame', cnf, {}, extra)

class AppLayout:

	def __init__(self, master):
		
		self.choose_directory = os.getcwd()
		self.choose_file	  = os.getcwd()

		
		# extensionFrame = LabelFrame(master, text='SELECTED EXTENSION', bg='gray')

		l_frame_settings  = LabelFrame(master, text='SETTINGS', bg='gray')
		frame_settings    = Frame(l_frame_settings, bd=5, bg='blue')
		# self.ent_cdir = Entry(frame_settings, bg='green', width=100)
		
		self.combo_extension_val = ('.png', '.jpg', '.pdf', '.xlsx', '.xls', '.doc', '.docx', '.epf', '.erf', 'ALL FILE EXTENSIONS')	
		self.combo_extension = ttk.Combobox(frame_settings, width=11, values=self.combo_extension_val, state=NORMAL)
		self.combo_extension.bind("<<ComboboxSelected>>", self.selectedExtension)
		self.combo_extension.current(0)
		self.combo_extension.pack(side=LEFT)
			
		self.debug_mode = IntVar(); self.debug_mode.set(1)
		# position = {"padx":6, "pady":6, "anchor":NW}
		debug_mode_checkbutton = ttk.Checkbutton(frame_settings, text="DEBUG MODE", variable=self.debug_mode, command=self.selectDebug)
		# debug_mode_checkbutton.pack(**position)
		debug_mode_checkbutton.pack(side=RIGHT)
		
		frame_settings.pack(anchor=SW, fill=X)
		l_frame_settings.pack(fill=X)


		l_frame_navigator = LabelFrame(master, text='NAVIGATOR', bg='gray')

		frame_lbl_display    = Frame(l_frame_navigator, bd=5, bg='orange')
		self.lbl_display  = Label(frame_lbl_display, text=self.choose_directory, fg='white', bg='gray', justify=LEFT)  # , width=73, height=1
		self.lbl_display.pack(side=LEFT, fill=X)
		
		frame_lbl_display.pack(anchor=CENTER, fill=X) # pack(side=LEFT, anchor=W) 

		frame_btn_command    = Frame(l_frame_navigator, bd=5, bg='red')
		self.btn_cdir = Button(frame_btn_command, text='OPEN DIR',  width=11, command=self.chooseDirectory)
		self.btn_cdir.pack(side=RIGHT, anchor=E)
		
		self.btn_open = Button(frame_btn_command, text='OPEN FILE', width=11, command=self.chooseFile)
		self.btn_open.pack(side=RIGHT, anchor=E)
		
		self.btn_save = Button(frame_btn_command, text='SAVE FILE', width=11, command=self.saveFile)
		self.btn_save.pack(side=RIGHT, anchor=E)
		
		self.btn_find = Button(frame_btn_command, text='FIND',  width=11, command=self.findDoubles)
		self.btn_find.pack(side=RIGHT, anchor=E)

		
		frame_btn_command.pack(anchor=CENTER, fill=X) # E: положение в правой части контейнера по центру
		l_frame_navigator.pack(fill=X)


		l_frame_textarea     = LabelFrame(master, text='TXT AREA', bg='gray')
		self.txt    = Text(l_frame_textarea, bg='#cdcdcd', wrap=NONE)
		
		
		scrollY      = Scrollbar(l_frame_textarea, command=self.txt.yview)
		scrollX      = Scrollbar(l_frame_textarea, orient=HORIZONTAL, command=self.txt.xview)

		scrollY.pack(side=RIGHT, fill=Y)
		scrollX.pack(side=BOTTOM, fill=X)
		
		self.txt.config(yscrollcommand=scrollY.set)
		self.txt.config(xscrollcommand=scrollX.set)
		
		self.txt.pack(expand=1, fill=BOTH)
		
		l_frame_textarea.pack(expand=1, fill=BOTH)

		

		# self.ent_cdir.pack(side=LEFT, fill=X)


		
		# self.btn_save.pack(anchor=NE)
		# self.btn_cdir.pack(anchor=NE)
		# self.btn_find.pack(side=RIGHT, anchor=W)
		
		
		
		
		

		
		
		
		
		
		

		
		# extensionFrame.pack(fill=X)
		
		
		
		# side: выравнивает виджет по одной из сторон контейнера RIGHT (выравнивание по правой стороне), W: положение в левой части контейнера по центру
		self.getIgnorExtensions()
	
	def openThread(self, settings):
		_thread.start_new_thread(self.setFields, (settings,))
	
	
	def setFields(self, settings):
		print(settings, type(settings))
		# self.txt.delete(1.0, END)	
		# for i in range(len(listMD5)):
		self.txt.insert(END, settings + '\n')
		# self.txt.insert(END, '\n')
					
		# self.sale_name.delete(0, END)
		# self.sale_name.insert(0, settings['name'])
		# self.sale_address.delete(0, END)
		# self.sale_address.insert(0, settings['address'])
		# self.cash_model.current(settings['model'])
	
		
	def getIgnorExtensions(self):
		filename = os.path.join(self.choose_directory, 'ignore extensions from list.txt') 
		with open(filename, 'r', encoding='UTF-8') as f_hd:
			# list_of_string = f_hd.read()	# <class 'str'>
			list_of_val_with_line_breaks = f_hd.readlines()	# <class 'list'>
		# print(list_of_val_with_line_breaks, type(list_of_val_with_line_breaks))
		list_of_values = [value.rstrip('\n') for value in list_of_val_with_line_breaks]
	
		# print(list_of_values, type(list_of_values))
		
		except_extension.extend(list_of_values)
		
		# print(except_extension, type(except_extension))
	
	
	def selectDebug(self):
		if self.debug_mode.get() == 1:
			showinfo(title="Info", message="Режим отладки включен")
		else:
			showinfo(title="Info", message="Режим отладки отключен")
		
	def selectedExtension(self, event):
		selection = self.combo_extension.get()
		# print(selection, type(selection))
		return selection


	def chooseFile(self):     
		filetypes = (("Текстовый файл", "*.txt"), ("Изображение", "*.jpg *.gif *.png"), ("Любой", "*"))
		filename = fd.askopenfilename(title="Открыть файл", initialdir=self.choose_file, filetypes=filetypes)
		# MD5 = []
		if filename:
			# self.ent_cdir.delete(0, END)
			# self.ent_cdir.insert(0, filename)
			self.lbl_display['text'] = filename
			self.txt.delete(1.0, END)
			with open(filename, 'r', encoding='UTF-8') as f_hd:
				self.txt.insert(1.0, f_hd.read()) 
				# список_строк = f_hd.readlines()
				# MD5.append(f_hd.read())
			# строки_без_переносов = [строка.rstrip('\n') for строка in список_строк]
		
			# print(строки_без_переносов, type(строки_без_переносов))
			
			# self.txt.insert(1.0, f_hd.read())
			# f_hd = open(filename, encoding='utf-8') # encoding='utf-8'
			# self.txt.insert(1.0, f_hd.read())
			# f_hd.close()

	def saveFile(self):
		contents = self.txt.get(1.0, END)
		new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"),))
		
		if new_file:
			new_file.write(contents)
			new_file.close()

	def chooseDirectory(self):
		directory = fd.askdirectory(title="Открыть папку", initialdir=self.choose_directory)
		
		if directory:
			self.lbl_display['text'] = directory
			self.choose_directory = directory
			# self.walk(directory)
			
		# for i in range(len(listMD5)):
			# self.txt.insert(END, listMD5[i])
			# self.txt.insert(END, '\n')
			
	def findDoubles(self):
		directory = self.lbl_display['text']
			
		if directory:
			try:
				if os.path.isdir(directory):
					listMD5.clear()
					self.walk(directory)
				else:
					showinfo(title="Info", message=f"Системе не удается найти указанный путь: '{directory}'")
					
				# self.txt.delete(1.0, END)	
				# for i in range(len(listMD5)):
					# self.txt.insert(END, listMD5[i])
					# self.txt.insert(END, '\n')
				
			except FileNotFoundError as e:
				logs.logWrite(f"FileNotFoundError {e}")
	
	
	def walk(self, dirname):
		print(f"Curent dir: {dirname}")
		
		dMode = True
		xList = listMD5
		
		for name in os.listdir(dirname):

			try:
				
				path = os.path.join(dirname, name)
				
				if os.path.isfile(path):
					# print(f"path: {path}")
					# txtQuit('q')
					

					basename, extension = os.path.splitext(path)
					# print(f"extension: {extension}")
					# txtQuit('q')
					
					if extension in except_extension:
						print(f"Расширение {extension} в списке игнорируемых.") 
						continue
						
					file_size = os.path.getsize(path)
					
					if not file_size > 0:
						print(f"Размер файла {path}: {file_size} байт", type(file_size))
						continue

					# if len(inputExtension) > 0:
						# if inputExtension.upper() != extension.upper():
							# print("Расширения не совпадают", "inputExtension =", inputExtension.upper(), "и extension =", extension.upper())
							# continue
					inputExtension = self.selectedExtension(self)
					
					if inputExtension != 'ALL FILE EXTENSIONS':
						if inputExtension.upper() != extension.upper():
							print("Расширения не совпадают", "inputExtension =", inputExtension.upper(), "и extension =", extension.upper())
							continue
					
					try:
						
						result = subprocess.run(
							['Certutil', '-hashfile', path, 'SHA1'],			# Command and arguments 
							capture_output=True,  						# Capture stdout and stderr
							text=True,  								# Decode output as text
							check=True  								# Raise CalledProcessError on non-zero exit code
						)

						# result = subprocess.run(['Certutil', '-hashfile', path, 'MD5'], capture_output=True, text=True, check=True)
						# print(list(result.returncode))
						if result.returncode == 0:
							# print(len(xList), " ", result.stdout.splitlines()[1])
							# print(len(xList))
							if result.stdout.splitlines()[1] in xList: #  xList.index(result.stdout.splitlines()[1]):
								
								try:
									index = xList.index(result.stdout.splitlines()[1])
									print("xList count", len(xList), f"Index [{index}]", f"find {result.stdout.splitlines()[1]}", path)
									# print()
									# print(f"dMode {dMode}", dMode)
									
									if self.debug_mode.get() != 1:
										# dst = os.remove(path)
										print("dst, 'move file in', path")
									
								except ValueError as e:
									print(f"ValueError {e}")
								
							else:
								# x.append(result.stdout.splitlines()[1])
								# print(result.stdout.splitlines()[1], path)
								# self.txt.insert(END, [result.stdout.splitlines()[1], path])
								# self.txt.insert(END, '\n')
								# self.txt.get(1.0, END)
								self.openThread(result.stdout.splitlines()[1])
								xList.append(result.stdout.splitlines()[1])
								
					except subprocess.CalledProcessError as e:
						print(f"Command failed with error: {e}")
						# print("Stderr:", e.stderr)
						# print(e.stderr)
						logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")
					
				else:
					if os.path.isdir(path):
						# print(f"Jamp {path}")
						self.walk(path)
			except PermissionError as e:
				logs.logWrite(f"PermissionError {e}")
				continue


root = Tk()

# Установка отображения формы в центре экрана
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3.5

root.wm_geometry("+%d+%d" % (x, y))

obj = AppLayout(root)



root.mainloop() 




# Параметр anchor помещает виджет в определенной части контейнера. Может принимать следующие значения:

    # n: положение вверху по центру

    # e: положение в правой части контейнера по центру

    # s: положение внизу по центру

    # w: положение в левой части контейнера по центру

    # nw: положение в верхнем левом углу

    # ne: положение в верхнем правом углу

    # se: положение в нижнем правом углу

    # sw: положение в нижнем левом углу

    # center: положение центру
