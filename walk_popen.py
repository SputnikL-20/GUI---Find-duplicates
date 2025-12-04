import os
import configparser


config = configparser.ConfigParser()
config.read('./sample.ini', encoding='utf8')
# print(config['APP']['log_txt'])
# print(config['APP']['suffix'])
# print(config['APP']['search'])

cwd  = os.getcwd() # current dir
f_hd = cwd + '\\' + config['APP']['log_txt']

# print(f_hd)

f_out = open(f_hd, 'wt', encoding='utf8')	
suffix = config['APP']['suffix']
	

def walk(dirname):

	global f_out, suffix
	
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			# print(path.split('.')[-1].lower())
			if path.split('.')[-1].lower() == suffix:
				# print(path)
				cmd = 'Certutil -hashfile "' + path + '" MD5'
				fp = os.popen(cmd)
				res = fp.read()
				# print(res)
				f_out.writelines(res)
				fp.close()
		else:
			walk(path)


walk( r'' + config['APP']['search'] )
f_out.close()

import find_double