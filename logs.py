from   datetime import datetime
from   tkinter.messagebox import showwarning
import os


def logWrite(log):
	try:
		with open(os.path.join(os.getcwd(), 'file-log.log'), 'a', encoding='UTF-8') as f:
			print(datetime.now(), f'{str(log)}', file=f)
	except PermissionError as e:
		showwarning(title="Внимание", message="Запустите программу от имени Администратора. Или добавте прав на чтение и запись директории программы cashier.")