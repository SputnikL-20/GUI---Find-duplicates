import os
import shutil
from find_double import cwd, config, spisok

v_dict = {}

for i in range(len(spisok)):
	if i % 2 != 0:
		v_dict[spisok[i]] = spisok[i - 1]
		
# for k, v in v_dict.items():
	# print(k, v)


mydir = cwd + '\\' + config['APP']['temp_d']

if not os.path.exists(mydir): os.makedirs(mydir)

directory = mydir + '\\'

print('Directory created ' + directory)

# moving files temporaly directory
for v in v_dict.values():
	# print(v[8:-1])
	move_a_file = v[8:-1]
	out_file    = v[8:-1].split('\\')[-1]
	# print(r'' + directory + out_file + '')
	# print(move_a_file, directory + out_file)
	if os.path.exists(move_a_file) and os.path.exists(directory):
		shutil.move(r'' + move_a_file + '', r'' + directory + out_file + '')

# delete files
for j in range(len(spisok)):
	if j % 2 == 0:
		if os.path.isfile(spisok[j][8:-1]):
			os.remove(r'' + spisok[j][8:-1])
			print('Remove success: ' + spisok[j][8:-1])
		else:
			print("File doesn't exists! " + spisok[j][8:-1])

			
user_move = input('\nRemove log file? ' + cwd + '\\' + config['APP']['log_txt'] + '\n1 - Yes, 2 - No: ')

if int(user_move) == 1:
	os.remove(r'' + cwd + '\\' + config['APP']['log_txt'])




