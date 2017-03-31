import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.50.12',port=22, username = 'ubuntu', password = 'Nexii@123')
sftp = ssh.open_sftp()
sftp.put('Project1.py', '/home/ubuntu/test/software/Project1.py')
sftp.get('/home/ubuntu/test/software/IAM.txt' , 'IAM.txt')
stdin, stdout, stderr = ssh.exec_command('ls -l')
output = stdout.readlines()
print stdout.readlines()

ssh.close()
