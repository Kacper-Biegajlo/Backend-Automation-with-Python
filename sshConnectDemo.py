import paramiko as paramiko
import csv
from utilities.configurations import *

# Start connection
username = getConfig()['SERVER']['username']
password = getConfig()['SERVER']['password']
host = getConfig()['SERVER']['host']
port = getConfig()['SERVER']['port']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Run commands
# stdin, stdout, stderr = ssh.exec_command('ls -a')
# stdin.close()
stdin, stdout, stderr = ssh.exec_command('cat demofile')
stdin.close()
# print(stdout.readlines())
lines = stdout.readlines()
print(lines[1])

# Upload files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath, destinationPath)

sftp = ssh.open_sftp()
destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath, destinationPath)

# Trigger the Batch commands
stdin, stdout, stderr = ssh.exec_command('python script.py')
stdin.close()

# Download the file to local system
sftp.get('loanasa.csv','outputFiles/loanasa.csv')

# Parse output file csv
with open('outputFiles/loanasa.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if row[0] == '32321':
            assert row[1] == 'rejected'



ssh.close()