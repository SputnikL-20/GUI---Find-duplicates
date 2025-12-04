import os
import sys
import shutil

spisok = []
# move_spisok = []
# full_spisok = []

v_dict = {}
log_txt_file = './dataNewTMP2.txt'

for i in open(log_txt_file):
	spisok.append(i.strip())
	if 'CertUtil: -hashfile — команда успешно выполнена.' in spisok:
		spisok.remove('CertUtil: -hashfile — команда успешно выполнена.')		


	
for i in range(len(spisok)):
	if i % 2 != 0:
		v_dict[spisok[i]] = spisok[i - 1]
		
				
tmp_dir = r'C:\Work\tmp' + '\\'

# moving files temporaly directory
for v in v_dict.values():
	# print(v[8:-1])
	move_a_file = v[8:-1]
	out_file    = v[8:-1].split('\\')[-1]
	# print(move_a_file, tmp_dir, out_file)
	if os.path.exists(move_a_file) and os.path.exists(tmp_dir):
		shutil.move(r'' + move_a_file + '', r'' + tmp_dir + out_file + '')

# Get directory name
mydir = r'C:\Users\Заря\Pictures\by_old_android'
# Try to remove the tree; if it fails, throw an error using try...except.
try:
    shutil.rmtree(mydir) # remove directory and contents
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
	
# create new directory
if not os.path.exists(mydir):
	os.makedirs(mydir)

# moving files new directory
for v in v_dict.values():
	# print(v[8:-1])
	move_a_file = v[8:-1]
	out_file    = v[8:-1].split('\\')[-1]
	# print(move_a_file, tmp_dir, out_file)
	if os.path.exists(tmp_dir + out_file) and os.path.exists(mydir):
		shutil.move(r'' + tmp_dir + out_file + '', r'' + move_a_file + '')
	
# for k, v in v_dict.items():
	# print(k, v)
		
# for i in range(len(spisok)):
	# if i % 2 != 0:
		# for j in range(i + 1, len(spisok)):
			# if j % 2 != 0:
				# if spisok[i] in spisok[j]:
					# move_spisok.append(spisok[i - 1][8:-1])
					# move_spisok.append(spisok[j - 1][8:-1])
					# print(spisok[i - 1])
					# print(spisok[j - 1]) 
					# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
					# print(spisok[i - 1], spisok[i - 1][8:-1])
					# print(spisok[i - 1], spisok[i - 1].split('\\')[-1][0:-1])
					# print(spisok[j - 1], spisok[i - 1].split('\\')[-1][0:-1]) 
					
# for i in range(len(move_spisok)):
	# print(move_spisok[i])
	
	
# for i in range(len(spisok)):
	# if i % 2 != 0:
		# for j in range(i + 1, len(spisok)):
			# if j % 2 != 0:
				# if spisok[i] in spisok[j]:
					# full_spisok.append(spisok[i - 1][8:-1])
					# full_spisok.append(spisok[i])
					# full_spisok.append(spisok[j - 1][8:-1])
					# full_spisok.append(spisok[j])
					
# for i in range(len(full_spisok)):
	# print(full_spisok[i])

			
# j = 0				
# for i in range(len(move_spisok)):
	# print(move_spisok[i])
	# print(os.path.abspath(move_spisok[i]))
	# in_file = r"" + move_spisok[i] + ""
	# in_file = move_spisok[i]
	# to_dir = 'C:\Work\pdf'
	# to_dir = r'C:\Users\Заря\Pictures\by_old_android'
	# m_file = to_dir + '\\' + move_spisok[i].split('\\')[-1]

	# if os.path.exists(in_file) and os.path.exists(to_dir):
		# if os.path.exists(m_file):
			# m_file = r"" + to_dir + "\\" + str(j) + move_spisok[i].split('\\')[-1] + ""
			# shutil.move(in_file, m_file)
		# shutil.move(in_file, m_file)
			# j += 1
		# else:
			# shutil.move(in_file, m_file)
			
	# print(in_file, m_file)

	# shutil.move(r"C:\ПЕРЕМЕСТИТЬ\MyAndroid\Файлы\Съемный диск\WhatsApp\Media\WhatsApp Images\Sent\IMG-20170223-WA0007.jpg", r"C:\Work\tmp\IMG-20170223-WA0007.jpg")