import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ip = raw_input('Enter the IP: ')
#Port = input('Enter the Port Number: ')
#Username = raw_input('Enter the Username: ')
#Password = raw_input('Enter the Password: ')
#ssh.connect(ip,port=Port,username=Username,password=Password)
ssh.connect('192.168.50.12', port=22, username='ubuntu', password='Nexii@123')
stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n ls')
print "projects list:\n",stdout.read()
a = raw_input("Select your project: ")
stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n cd {0} \n ls'.format(a))
softwares = stdout.read()

print '\nThe Softwares present in the selected project %s are: \n'%(a),softwares

stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n cd {0} \n pwd'.format(a))
pwd = stdout.read()
pwd=pwd.strip('\n')

b = raw_input("Select the software you want to download:")
sftp = ssh.open_sftp()
remote_file_path = r"{0}/{1}".format(pwd,b)
sftp.get(remote_file_path,b)
print "You have successfully downloaded"
ssh.close()
