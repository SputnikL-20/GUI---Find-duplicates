import subprocess

# Команда для выполнения в PowerShell
command = ["powershell.exe", "-Command", "Get-ChildItem C:\\"]

# Запуск процесса и получение результата
result = subprocess.run(command, capture_output=True, text=True, encoding="cp866") # или utf-8 для PS Core

print("Вывод:\n", result.stdout)
if result.stderr:
	print("Ошибка:\n", result.stderr)