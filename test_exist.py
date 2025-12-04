import os

in_file = 'C:\ПЕРЕМЕСТИТЬ\MyAndroid\data\AliveShare\photo\IMG_20150710_105834.jpg'

if os.path.exists(r'' + in_file + ''):
# if os.path.isfile(r'C:\ПЕРЕМЕСТИТЬ\MyAndroid\data\AliveShare\photo\1015697_31183803.jpg'):
	print('true')
	print(in_file)
else:
	print('false')