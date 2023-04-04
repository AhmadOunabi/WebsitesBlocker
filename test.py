import subprocess
# host = "C:\Windows\System32\drivers\etc\hosts"
# temp_host= "hosts"
command = ["runas", "/user:Administrator", "python", "test.py"]

# run the command and pass the password for the Administrator account when prompted
subprocess.call(command)
host="C:\Windows\System32\drivers\etc\hosts"

with open(host,'r+') as file:
    file.read()