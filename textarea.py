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
	

DebugMode		= True
finalCatalog 	= ''
selected_extension 	= '.pdf'
# availableExtensions = ['.jpg', '.png', '.cfe', '.cfu', '.epf']
except_extension = [] # ['.cfl', '.7z', '.lnk', '.avif', '.dthumb', '.INI', '.HTML']
listMD5 		= []




def txtQuit(q):
	if q == 'q':
		print('EXIT PROGRAMM')
		quit()
		

def txtDebug(val = ''):	
	if len(val) > 0 and val.upper() == 'Y':
		print('Install mode: --> DEBUG PROGRAMM')
		return True
	return False
	
def extUpper(extension):
	return extension.upper()





# Widget.__init__(self, master, 'frame', cnf, {}, extra)

class AppLayout:

	def __init__(self, master):
		
		self.choose_directory = os.getcwd()
		self.choose_file	  = os.getcwd()
		
		self.master = master

		
		# extensionFrame = LabelFrame(master, text='SELECTED EXTENSION', bg='gray')

		l_frame_settings  = LabelFrame(master, text='SETTINGS', bg='gray')
		frame_settings    = Frame(l_frame_settings, bd=5, bg='blue')
		# self.ent_cdir = Entry(frame_settings, bg='green', width=100)
		
		self.combo_extension_val = ('.PNG', '.JPG', '.PDF', '.XLSX', '.XLS', '.DOC', '.DOCX', '.MP3','.EPF', '.ERF', '.AVI', 'ALL FILES')	
		self.combo_extension = ttk.Combobox(frame_settings, width=15, values=self.combo_extension_val, state=NORMAL)
		self.combo_extension.bind("<<ComboboxSelected>>", self.selectedExtension)
		self.combo_extension.current(0)
		self.combo_extension.pack(side=LEFT)
			
		self.debug_mode = IntVar()
		self.debug_mode.set(1)
		self.debug_mode_checkbutton = ttk.Checkbutton(frame_settings, text="DEBUG MODE", variable=self.debug_mode, command=self.selectDebug)
		# position = {"padx":6, "pady":6, "anchor":NW}
		# self.debug_mode_checkbutton.pack(**position)
		self.debug_mode_checkbutton.pack(side=RIGHT)
		
		self.include_nested_dir = IntVar()
		self.include_nested_dir.set(0)
		self.include_nested_dir_checkbutton = ttk.Checkbutton(frame_settings, text="INCLUDE NESTED DIRECTORIES", variable=self.include_nested_dir, command=self.getSettingNestedDir)
		position = {"padx":6, "pady":6, "anchor":E, "side":RIGHT}; 
		self.include_nested_dir_checkbutton.pack(**position)
		
		
		frame_settings.pack(anchor=SW, fill=X)
		l_frame_settings.pack(fill=X)


		l_frame_navigator = LabelFrame(master, text='NAVIGATOR', bg='gray')

		frame_lbl_display    = Frame(l_frame_navigator, bd=5, bg='orange')
		self.lbl_display  = Label(frame_lbl_display, text=self.choose_directory, fg='white', bg='gray', justify=LEFT)  # , width=73, height=1
		self.lbl_display.pack(side=LEFT, fill=X)
		
		# frame_lbl_display_test    = Frame(l_frame_navigator, bd=5, bg='orange')
		# self.lbl_display_test  = Label(frame_lbl_display_test, text='TEST', fg='white', bg='gray', justify=LEFT)
		# self.lbl_display_test.pack(side=LEFT, fill=X)
		
		
		
		frame_lbl_display.pack(anchor=CENTER, fill=X) # pack(side=LEFT, anchor=W) 
		# frame_lbl_display_test.pack(anchor=CENTER, fill=X) 

		frame_btn_command    = Frame(l_frame_navigator, bd=5, bg='red')
		
		self.btn_checksum = Button(frame_btn_command, text='SHA-512 CHECKSUM', width=20, command=self.checksumFile)
		self.btn_checksum.pack(side=LEFT, anchor=W)
		
		self.btn_logs = Button(frame_btn_command, text="View Log'S", width=11, command=self.loadLogTxt)
		self.btn_logs.pack(side=LEFT, anchor=W)
		
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
		self.txt    = Text(l_frame_textarea, bg='#cdcdcd', fg='blue', wrap=NONE)
		
		
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
		
		
		
		
		

		self.xListPath = []
		
		
		
		
		

		
		# extensionFrame.pack(fill=X)
		
		
		
		# side: выравнивает виджет по одной из сторон контейнера RIGHT (выравнивание по правой стороне), W: положение в левой части контейнера по центру
		# self.getIgnorExtensions()
	
	# def openThread(self, settings):
		# _thread.start_new_thread(self.setFields, (settings,))
	
	
	def setFields(self, path):
		self.txt.delete(1.0, END)   # Очистка textarea
		self.lock_ui()
		print(f"Поиск в дирректории: {path}")
		logs.logWrite(f"Поиск в дирректории: {path}")
		listMD5.clear()
		self.xListPath = []
		self.walk(path)
		self.unlock_ui()
		showinfo(title="", message="Спасибо! Поиск закончен.")
		logs.logWrite(f"Поиск закончен...\n")
		# breakpoint()
		# 	
		# for i in range(len(listMD5)):
		# self.lbl_display_test['text'] = path
		# 
		# self.txt.insert(END, '\n')
					
		# self.sale_name.delete(0, END)
		# self.sale_name.insert(0, path['name'])
		# self.sale_address.delete(0, END)
		# self.sale_address.insert(0, path['address'])
		# self.cash_model.current(path['model'])
	
	
	def loadLogTxt(self):	
		filename = os.path.join(os.getcwd(), 'file-log.log')
		if os.path.isfile(filename):
			# Очищаем поле текстового документа
			self.txt.delete(1.0, END)
			# читаем построчно с помощью `for`
			with open(filename, 'r', encoding='UTF-8') as f_hd:
				for line in f_hd:
					# Вставляем строку в конец списка
					self.txt.insert(END, line)
	
	
	def getIgnorExtensions(self):
		filename = os.path.join(self.choose_directory, 'ignore_extensions.dat') 
		with open(filename, 'r', encoding='UTF-8') as f_hd:
			# list_of_string = f_hd.read()	# <class 'str'>
			list_of_val_with_line_breaks = f_hd.readlines()	# <class 'list'>
		# print(list_of_val_with_line_breaks, type(list_of_val_with_line_breaks))
		list_of_values = [value.rstrip('\n').upper() for value in list_of_val_with_line_breaks]
		# print(list_of_values, type(list_of_values))		
		except_extension.extend(list_of_values)
		logs.logWrite(f"Список игнорируемых расширений: {except_extension}")
	
	
	def selectDebug(self):
		if self.debug_mode.get() == 1:
			showinfo(title="Info", message="Режим отладки включен")
		else:
			showinfo(title="Info", message="Режим отладки отключен")
			
	def getSettingNestedDir(self):
		if not self.include_nested_dir.get() == 1:
			# showinfo(title="Info", message="Будет выполнен поиск во вложенных каталогах")
		# else:
			showinfo(title="Info", message="Поиск во вложенных каталогах отключен")
		
	def selectedExtension(self, event):
		extension = self.combo_extension.get()
		# print(extension, type(extension))
		return extension


	def checksumFile(self):     
		filetypes = (("Любой", "*"), ("Текстовый файл", "*.txt"), ("Изображение", "*.jpg *.gif *.png"))
		filename = fd.askopenfilename(title="Открыть файл", initialdir=self.choose_file, filetypes=filetypes)
		# MD5 = []
		if filename:
			# self.ent_cdir.delete(0, END)
			# self.ent_cdir.insert(0, filename)
			self.lbl_display['text'] = filename
			# self.txt.delete(1.0, END)
			# with open(filename, 'r', encoding='UTF-8') as f_hd:
				# self.txt.insert(1.0, f_hd.read()) 
				# список_строк = f_hd.readlines()
				# MD5.append(f_hd.read())
			# строки_без_переносов = [строка.rstrip('\n') for строка in список_строк]
		
			# print(строки_без_переносов, type(строки_без_переносов))
			
			# self.txt.insert(1.0, f_hd.read())
			# f_hd = open(filename, encoding='utf-8') # encoding='utf-8'
			# self.txt.insert(1.0, f_hd.read())
			# f_hd.close()
			
			
			path = filename	
				
			if os.path.isfile(path):
				# print(f"path: {path}")
				# txtQuit('q')
				

				basename, extension = os.path.splitext(path)
				print(f"extension: {extension} basename: {basename}")
				# txtQuit('q')
				
				# if extension in except_extension:
					# print(f"Расширение {extension} в списке игнорируемых.") 
					# continue
					
				
					
				file_size = os.path.getsize(path)
				
				if file_size > 0:
					# print(f"Размер файла {path}: {file_size} байт", type(file_size))

				# if len(selected_extension) > 0:
					# if selected_extension.upper() != extension.upper():
						# print("Расширения не совпадают", "selected_extension =", selected_extension.upper(), "и extension =", extension.upper())
						# continue
				# selected_extension = self.selectedExtension(self)
				
				# if selected_extension != 'ALL FILE EXTENSIONS':
					# if selected_extension.upper() != extension.upper():
						# print("Расширения не совпадают", "selected_extension =", selected_extension.upper(), "и extension =", extension.upper())
						# continue
					
					checksum_file = self.getChecksum(path, 'SHA512')
					if checksum_file != 0:
						self.txt.delete(1.0, END)
						self.txt.insert(END, checksum_file + '\n')
					
					# try:
						
						# result = subprocess.run(
							# ['Certutil', '-hashfile', path, 'SHA512'],	# Command and arguments 
							# capture_output=True,  						# Capture stdout and stderr
							# text=True,  								# Decode output as text
							# check=True  								# Raise CalledProcessError on non-zero exit code
						# )

						# result = subprocess.run(['Certutil', '-hashfile', path, 'MD5'], capture_output=True, text=True, check=True)
						# print(list(result.returncode))
						# if result.returncode == 0:
							# self.txt.delete(1.0, END)
							# self.txt.insert(END, result.stdout.splitlines()[1] + '\n')
							# self.txt.insert(END, os.path.dirname(path) + '\n')
							
							# file_name = os.path.basename(path) # Вывод: my_file.txt
							# file_checksum = os.path.join(os.path.dirname(path), file_name + '_Контрольная сумма SHA-512.dat')
							# if os.path.isfile(saved_file):
							# with open(file_checksum, 'w', encoding='UTF-8') as f_hd:
								# f_hd.write(result.stdout.splitlines()[1])
				
								
					# except subprocess.CalledProcessError as e:
						# print(f"Command failed with error: {e}")
						# print("Stderr:", e.stderr)
						# print(e.stderr)
						# logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")
				else:
					showinfo(title="Info", message="Файл без данных!")
			# else:
				# if self.include_nested_dir.get() != 0:
					# if os.path.isdir(path):
						# self.walk(path)		# print(f"Jamp {path}")
						
						
	def getChecksum(self, path, check):
		
		checksum_file = 0
				
		try:		
			result = subprocess.run(
				['Certutil', '-hashfile', path, check],		# Command and arguments 
				capture_output=True,  						# Capture stdout and stderr
				text=True,  								# Decode output as text
				check=True  								# Raise CalledProcessError on non-zero exit code
			)

			if result.returncode == 0:
				checksum_file = result.stdout.splitlines()[1]				
					
		except subprocess.CalledProcessError as e:
			print(f"Command failed with error: {e}")
			logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")
			
		return checksum_file



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
		saved_file = self.lbl_display['text']
		
		if os.path.isfile(saved_file):
			with open(saved_file, 'w', encoding='UTF-8') as f_hd:
				f_hd.write(contents)
		else:
			new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"), ("Тестовый файл", "*.dat")))			
			if new_file:
				new_file.write(contents)
				new_file.close()
	
	
	def chooseDirectory(self):
		
		dir = fd.askdirectory(title="Выбрать папку для поиска файлов", initialdir=self.choose_directory)
		
		if os.path.isdir(dir):
			self.lbl_display['text'] = dir
			self.choose_directory = dir
	
	
	def findDoubles(self):
		
		directory = self.lbl_display['text']
	
		if os.path.isdir(directory):
			try:
				self.openThread(directory)
			except FileNotFoundError as e:
				logs.logWrite(f"FileNotFoundError {e}")
		else:
			showinfo(title="Info", message=f"Системе не удается найти указанный путь: '{directory}'")
	
	
	def openThread(self, directory):
		_thread.start_new_thread(self.setFields, (directory,))
	
	
	def walk(self, dirname):
		
		DebugMode = True
		xList = listMD5
		# xListPath = []
		# print(len(xList))
		
		for name in os.listdir(dirname):

			try:
				
				path = os.path.join(dirname, name)
				
				if os.path.isfile(path):	#														Если это Файл ?			

					basename, extension = os.path.splitext(path)
					
					if len(extension) == 0:
						logs.logWrite(f"У файла отсутствует расширение. Путь к файлу: {path}")
						continue
					
					if extUpper(extension) in except_extension:
						logs.logWrite(f"Расширение {extension} в списке игнорируемых.") 
						continue
						
					file_size = os.path.getsize(path)

					if not file_size > 0:	#														... и Файл не больше ноля
						logs.logWrite(f"Размер файла {path}: не больше {file_size} байт. Тип переменной: {type(file_size)}")
						continue

					# if len(selected_extension) > 0:
						# if selected_extension.upper() != extension.upper():
							# print("Расширения не совпадают", "selected_extension =", selected_extension.upper(), "и extension =", extension.upper())
							# continue
					selected_extension = self.selectedExtension(self)
					
					if selected_extension != 'ALL FILES':					
						if extUpper(selected_extension) != extUpper(extension):
							logs.logWrite(f"Выбранное расширение для поиска файлов: {selected_extension}: не соответствует текущему: {extension}")
							continue
					
					try:
						
						result = subprocess.run(
							['Certutil', '-hashfile', path, 'SHA1'],	# Command and arguments 
							capture_output=True,  						# Capture stdout and stderr
							text=True,  								# Decode output as text
							check=True  								# Raise CalledProcessError on non-zero exit code
						)

						# result = subprocess.run(['Certutil', '-hashfile', path, 'MD5'], capture_output=True, text=True, check=True)
						# print(list(result.returncode))
						if result.returncode == 0:
							Code_SHA1 = result.stdout.splitlines()[1]
							
							if Code_SHA1 in xList:
								
								for iLisx in self.xListPath:
									for i in iLisx:
										if Code_SHA1 in i:
											str = f"Найдена копия файла: {iLisx[1]} в: {path}"
											self.txt.insert(END, str + '\n')
											logs.logWrite(str)
								
								try:
									index = xList.index(Code_SHA1)
									print("xList count", len(xList), f"Index [{index}]", f"find {Code_SHA1}", path)
									# print()
									# print(f"DebugMode {DebugMode}", DebugMode)
									
									if self.debug_mode.get() != 1:
										dst = os.remove(path)
										print(dst, 'move file in', path)
										str = f"REMOVE file in: " + path
										self.txt.insert(END, str + '\n')
									
								except ValueError as e:
									print(f"ValueError {e}")
								
							else:
								# x.append(result.stdout.splitlines()[1])
								# print(result.stdout.splitlines()[1], path)
								# self.txt.insert(END, (result.stdout.splitlines()[1], path))
								# self.txt.insert(END, '\n')
								# self.txt.get(1.0, END)
								# self.txt.insert(END, result.stdout.splitlines()[1] + '\n')
								# self.txt.insert(END, '\n')
								# self.lbl_display_test['text'] = result.stdout.splitlines()[1]
								# self.openThread(result.stdout.splitlines()[1])
								
								xList.append(Code_SHA1)
								
								# xListPath = [Code_SHA1, path]
								
								self.xListPath.append([Code_SHA1, path])
								
								# print(f"Количество в self.xListPath: {len(self.xListPath)}", f"Количество в xList: {len(xList)}")
								
					except subprocess.CalledProcessError as e:
						# print(f"Command failed with error: {e}")
						# print("Stderr:", e.stderr)
						# print(e.stderr)
						logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")
					
				else:
					if self.include_nested_dir.get() != 0:
						if os.path.isdir(path):
							self.walk(path)
					
			except PermissionError as e:
				logs.logWrite(f"PermissionError {e}")
				continue
				
		# breakpoint()
	
	
	def dismissApp(self):			
		self.master.quit()
		
	# def set_widgets_state(self, parent, state="disabled"):
		# for child in parent.winfo_children():
			# Рекурсивно проверяем вложенные фреймы
			# if child.winfo_children():
				# set_widgets_state(child, state)
			# try:
				# child.configure(state=state)
			# except:
				# Некоторые виджеты (например, Frame или Label) не имеют состояния state
				# print("DANDGER!")
				# pass
				
	# Функция блокировки всего интерфейса
	def lock_ui(self):
		# self.set_widgets_state(self.master, "disabled")
		state="disabled"
		self.btn_open.configure(state=state)
		self.btn_save.configure(state=state)
		self.btn_cdir.configure(state=state)
		self.btn_checksum.configure(state=state)
		self.btn_logs.configure(state=state)
		self.btn_find.configure(state=state)
		self.combo_extension.configure(state=state)

		self.lbl_display.configure(state=state)
		self.include_nested_dir_checkbutton.configure(state=state)
		self.debug_mode_checkbutton.configure(state=state)


	# Функция разблокировки
	def unlock_ui(self):
		# self.set_widgets_state(self.master, "normal")
		state="normal"
		self.btn_open.configure(state=state)
		self.btn_save.configure(state=state)
		self.btn_cdir.configure(state=state)
		self.btn_checksum.configure(state=state)
		self.btn_logs.configure(state=state)
		self.btn_find.configure(state=state)
		self.combo_extension.configure(state=state)

		self.lbl_display.configure(state=state)
		self.include_nested_dir_checkbutton.configure(state=state)
		self.debug_mode_checkbutton.configure(state=state)


# root = Tk()

# Установка отображения формы в центре экрана
# x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
# y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3.5

# root.wm_geometry("+%d+%d" % (x, y))

# obj = AppLayout(root)



# root.mainloop() 



def main():
	root = Tk()
	obj = AppLayout(root)

	root.title("GUI - Find duplicates")
	# root.iconbitmap(os.path.join(obj_cashier.cwd, 'src\\ico\\fptr_t.ico'))
	root.geometry("1100x600")
	# root.resizable(False, False)

	# Установка отображения формы в центре экрана
	x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3.5
	y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4

	root.wm_geometry("+%d+%d" % (x, y))
	root.protocol('WM_DELETE_WINDOW', obj.dismissApp)
	
	
	obj.getIgnorExtensions()
	
	root.mainloop()


if __name__=='__main__':
	logs.logWrite("Получаем ИД процесса: {} [{}]".format(os.getpid(), type(os.getpid())))
	main()




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
	
	
	
	
# from tkinter import *
# from tkinter import ttk
 
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200") 
 
 
# def on_modified(event):
    # label["text"]=editor.selection_get()
 
# editor = Text(height=8)
# editor.pack(fill=X)
# editor.bind("<<Selection>>", on_modified)
 
# label = ttk.Label()
# label.pack(anchor=NW)
 
# root.mainloop()
