from walk_popen import os, f_hd, cwd, config


log_txt_file = f_hd
spisok = []
move_spisok = []

for i in open(log_txt_file, encoding='utf8'):
	spisok.append(i.strip())
	if 'CertUtil: -hashfile — команда успешно выполнена.' in spisok:
		spisok.remove('CertUtil: -hashfile — команда успешно выполнена.')		


# print('Count', len(spisok) / 2)	

for i in range(len(spisok)):
	if i % 2 != 0:
		for j in range(i + 1, len(spisok)):
			if j % 2 != 0:
				if spisok[i] in spisok[j]:
					move_spisok.append(spisok[i - 1][8:-1])
					move_spisok.append(spisok[j - 1][8:-1])
					# print(spisok[i - 1])
					# print(spisok[j - 1]) 


print('Doubles:', len(move_spisok))


# import moving_remove_files
















