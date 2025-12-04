
import logs # import logWrite
import os
import shutil
import subprocess
# import sys
	

finalCatalog 	= ''
inputExtension 	= ''
availableExtensions = ['.jpg', '.png', '.cfe', '.cfu', '.epf']
exceptExtension = ['.cfl', '.dat']
listMD5 		= []
dMode			= False


def txtQuit(q):
	if q == 'q':
		print('EXIT PROGRAMM')
		quit()
		

def txtDebug(val = ''):
	
	if len(val) > 0 and val.upper() == 'Y':
		print('Install mode: --> DEBUG PROGRAMM')
		return True
	
	return False
	# txtQuit('q')
		
# txtDebug(d = modPragma)
	# if d == 'd':
		# dMode = True



def walk(dirname, dMode):
	print(f"Curent dir: {dirname}")
	# if dMode:
		# print('Mode --> DEBUG PROGRAMM')
		
	
	xList = listMD5
	print(xList)
	# cwd = os.getcwd()
	# f_out = open(os.path.join(cwd, 'dataMD5.txt'), 'w')
	# f_out.close()
	# print(cwd + r'\dataMD5.txt')
	# f_out = open(cwd + r'\dataMD5.txt', 'w')	
	# quit()
	for name in os.listdir(dirname):
		
		try:
			
			path = os.path.join(dirname, name)
			
			if os.path.isfile(path):
				
				# file_stats = os.stat(path)
				# print(file_stats)

				file_size = os.path.getsize(path)
				
				if not file_size > 0:
					print(f"Размер файла {path}: {file_size} байт", type(file_size))
					continue
				

				basename, extension = os.path.splitext(path)
				
				if extension in exceptExtension:
					continue

				if len(inputExtension) > 0:
					if inputExtension.upper() != extension.upper():
						# print("Расширения не совпадают", "inputExtension =", inputExtension.upper(), "и extension =", extension.upper())
						continue
				else:
					# print("Расширения не задано! Будет расчитан ХЭШ у всех файлов.")	
					print("")	
				
				try:
					# print(path)
					# cmd = ['Certutil -hashfile "' + path + '" MD5']
					# cmd = ["Certutil -hashfile", "r'" + path + "'", "MD5"]
					# print(cmd[0])
					# print(cmd[0])
					# fp = os.popen(cmd)
					# res = fp.read()
					
					result = subprocess.run(
						['Certutil', '-hashfile', path],			# Command and arguments 
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
								
								if not dMode:
									dst = os.remove(path)
									print(dst, 'move file in', path)
								# else:
									# dMode = 0
								
							except ValueError as e:
								print(f"ValueError {e}")
							# x = int(len(xList))
							# if xList[1] == result.stdout.splitlines()[1]:
								# x = 1
							# try:
								# dst = shutil.move(fileSearch, finalCatalog)
								# print(result.stdout.splitlines()[1], path)
								# print()
								# dst = os.remove(fileSearch)
								# print(dst, 'move file in', fileSearch)
							# except shutil.Error as e:
								# print(e)
								# logs.logWrite(f"Command failed with error - shutil.Error: {e}")
							# except PermissionError as e:
								# logs.logWrite(f"Command failed with error - PermissionError: {e}")
								# continue
							# else:
								# xList.append(result.stdout.splitlines()[1]) 
								# print(x)
								
								# if x == 0:
						else:
							# x.append(result.stdout.splitlines()[1])
							print(result.stdout.splitlines()[1], path)
							xList.append(result.stdout.splitlines()[1])
								
					# result = subprocess.Popen(cmd[0], stdout=subprocess.PIPE)
					# data = result.communicate()
					# print(str(data), type(data))
					# for line in data:
						# print(line)
					# res = subprocess.call(cmd)
					# f_out.writelines(result.stdout.splitlines()[1] + '\n')
					# fp.close()	
					
					# res = subprocess.run(['REGEDIT', '/S', os.path.join(self.cwd, 'key-cashier.reg')], shell=True) # Выполнится только в случае если программа запущена от имени Администратора
					# res = subprocess.run(['Certutil', '/hashfile', path, 'MD5'], shell=True) # Выполнится только в случае если программа запущена от имени Администратора
					# print(res, type(res))
					# logs.logWrite(result.stdout)
				except subprocess.CalledProcessError as e:
					print(f"Command failed with error: {e}")
					# print("Stderr:", e.stderr)
					# print(e.stderr)
					logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")
				
			else:
				if os.path.isdir(path):
					# print(f"Jamp {path}")
					walk(path, dMode)
		except PermissionError as e:
			logs.logWrite(f"PermissionError {e}")
			continue
	
	
def walkDestination(dirname):
	# quit()
	for filename in os.listdir(dirname):
		# print(dirname, filename)
		fileSearch = os.path.join(dirname, filename)
		# print(fileSearch)
		if os.path.isfile(fileSearch):
			# print(os.path.isfile(fileSearch)) # True
			# print(os.path.dirname(fileSearch))
			# print(os.path.isdir(fileSearch))
			
			try:
				result = subprocess.run(
					['Certutil', '-hashfile', fileSearch],		# Command and arguments (['Certutil', '-hashfile', fileSearch, 'MD5')
					capture_output=True,  						# Capture stdout and stderr
					text=True,  								# Decode output as text
					check=True  								# Raise CalledProcessError on non-zero exit code
				)
				# result = subprocess.run(['Certutil', '-hashfile', fileSearch, 'MD5'], capture_output=True, text=True, check=True)
				# print(list(result.returncode))
				if len(listMD5) == 0:
					txtQuit('q')

				listSearch = [string.rstrip('\n') for string in listMD5]
				
				if result.returncode == 0:
					# print(listSearch)
					# txtQuit('q')
					sumMd5 = result.stdout.splitlines()[1]
					
					if sumMd5 in listSearch:
						# print(fileSearch, finalCatalog)
						# logs.logWrite(str(list))
						# shutil.move(r'' + fileSearch + '', r'' + finalCatalog + '')
						# create new directory
						# mydir = os.path.dirname(finalCatalog) + "\\" + sumMd5
						# if not os.path.exists(mydir):
						# 	os.makedirs(mydir)
						try:
							# dst = shutil.move(fileSearch, finalCatalog)
							dst = os.remove(fileSearch)
							print(dst, 'move file in', fileSearch)
						except shutil.Error as e:
							# print(e)
							logs.logWrite(f"Command failed with error - shutil.Error: {e}")
						except PermissionError as e:
							logs.logWrite(f"Command failed with error - PermissionError: {e}")
							continue
						
							# basename, extension = os.path.splitext(fileSearch)
							# print(basename, extension)
							# declarePath = basename + "_" + sumMd5 + "_" + extension
							# os.renames(fileSearch, declarePath)
							# dst = shutil.move(declarePath, mydir)
							# logs.logWrite(dst)
						# except OSError as e:
						# try:
							# resultMove = subprocess.run(
								# ['move "' + path + " " + finalCatalog + '"'],					# Command and arguments 
								# capture_output=True,  						# Capture stdout and stderr
								# text=True,  								# Decode output as text
								# check=True  								# Raise CalledProcessError on non-zero exit code
							# )
						# except subprocess.CalledProcessError as e:
							# print(f"Command failed with error: {e}")
							# print("Stderr:", e.stderr)
							# print(resultMove.stderr)
							# logs.logWrite(resultMove.stderr)
					else:
						# try:
							# dst = shutil.move(fileSearch, finalCatalog)
							# print(dst, 'move file in', fileSearch)
						# except shutil.Error as e:
							# print(e)
							# logs.logWrite(f"Command failed with error - shutil.Error: {e}")
						# except PermissionError as e:
							# logs.logWrite(f"Command failed with error - PermissionError: {e}")
							# continue
						print('fileSearch - ', fileSearch)
						logs.logWrite(f"fileSearch - {fileSearch}")
						
					# listMD5.append(result.stdout.splitlines()[1] + '\n')
				# result = subprocess.Popen(cmd[0], stdout=subprocess.PIPE)
				# data = result.communicate()
				# print(str(data), type(data))
				# for line in data:
					# print(line)
				# res = subprocess.call(cmd)
				# f_out.writelines(result.stdout.splitlines()[1] + '\n')
				# fp.close()	
				
				# res = subprocess.run(['REGEDIT', '/S', os.path.join(self.cwd, 'key-cashier.reg')], shell=True) # Выполнится только в случае если программа запущена от имени Администратора
				# res = subprocess.run(['Certutil', '/hashfile', path, 'MD5'], shell=True) # Выполнится только в случае если программа запущена от имени Администратора
				# print(res, type(res))
				# logs.logWrite(result.stdout)
			except subprocess.CalledProcessError as e:
				print(f"Command failed with error: {e}")
				# print("Stderr:", e.stderr)
				# print(result.stderr)
				logs.logWrite(f"Raise CalledProcessError on non-zero exit code: {e}")	
		else:
			print('ELSE ', fileSearch)
			walkDestination(fileSearch)
	
	

# arg = 'C:\ПЕРЕМЕСТИТЬ\MyAndroid\QUMOSD32\Pictures'	
# arg = r'C:\Users\Заря\Videos\Клипы'	
# arg = r'C:\ПЕРЕМЕСТИТЬ\MyAndroid\Файлы\Фото'	
# arg = r'C:\Users\golikov.s\Pictures\bing'

finalCatalog = input('Destination final catalog: ').strip()
# print(finalCatalog, type(finalCatalog))
modePragma = input('Debug mode insert: Y or N?: ').strip()

dMode = txtDebug(modePragma)

inputExtension = input('Extension with at dot: ').strip()
txtQuit(inputExtension)

arg = finalCatalog	
walk(arg, dMode)

print(listMD5)

quit()
# txtQuit(finalCatalog)

# readHashSum = input('Read lines MD5? That enter name at extension for save fale: ')
# txtQuit(readHashSum)

# print(f"Final catalog: {finalCatalog}")

if len(readHashSum) > 0:
	with open('spam.txt', 'r') as file:
		# Используем readlines() для получения списка строк
		listMD5 = file.readlines()
else:
	arg = finalCatalog	
	walk(arg, dMode)

# print(listMD5)
finalList = input('Write lines MD5? That enter name at extension for save fale: ')
txtQuit(finalList)

if len(finalList) != 0:
	# cwd = os.getcwd()
	if len(listMD5) > 0:
		
		with open(finalList, 'w') as file:
			# for i in range(len(listMD5)):
			# stringList = str(listMD5).replace(']', '').replace('[', '')
			# file.write(stringList)
		
		# f_out = open(os.path.join(os.getcwd(), 'dataMD5.txt'), 'w')
		
		# for i in range(len(listMD5)):
			file.writelines(listMD5)
		
		# f_out.close()

		# print(cwd + r'\dataMD5.txt')
		# f_out = open(cwd + r'\dataMD5.txt', 'w')	
		# quit()

		# f_out.close()


	# Открываем файл для чтения
	with open('spam.txt', 'r') as file:
		# Используем readlines() для получения списка строк
		список_строк = file.readlines()

	# Теперь 'список_строк' содержит строки из файла
	строки_без_переносов = [строка.rstrip('\n') for строка in список_строк]
	# print(строки_без_переносов, type(строки_без_переносов))

	# if '50973dc749eeda50237f55b5a79fe145' in строки_без_переносов:
		# print('Find is')
	# f_out = open(os.path.join(os.getcwd(), 'spam.txt'), 'r')

	# print(str(list(f_out)), type(f_out))
	# f_out.close()


searchCatalog = input('Search catalog: ')
txtQuit(searchCatalog)

if os.path.exists(searchCatalog):
	walkDestination(searchCatalog)




# Example


# import subprocess

# try:
    # result = subprocess.run(
        # ["ls", "-l"],  # Command and arguments
        # capture_output=True,  # Capture stdout and stderr
        # text=True,  # Decode output as text
        # check=True  # Raise CalledProcessError on non-zero exit code
    # )
    # print("Command executed successfully:")
    # print("Stdout:", result.stdout)
    # print("Stderr:", result.stderr)
    # print("Return code:", result.returncode)
# except subprocess.CalledProcessError as e:
    # print(f"Command failed with error: {e}")
    # print("Stderr:", e.stderr)