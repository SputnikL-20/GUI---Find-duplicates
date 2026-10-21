import subprocess

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

command = ["powershell.exe", "-Command", "Get-Process"]
result = subprocess.run(
    command, 
    capture_output=True, 
    text=True, 
    startupinfo=startupinfo
)

print(result.stdout)
