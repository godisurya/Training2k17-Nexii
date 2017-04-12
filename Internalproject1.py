import smtplib
import getpass
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ip = raw_input('Enter the IP: ')
# Username = raw_input('Enter the Username: ')
# Password = raw_input('Enter the Password: ')
ssh.connect('192.168.50.12', port=22, username='ubuntu', password='Nexii@123')

role = raw_input("Select Admin/User: ")
if role == "User":
    stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n ls')
    print "projects list:\n", stdout.read()
    a = raw_input("Select your project: ")
    stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n cd {0} \n ls'.format(a))
    softwares = stdout.read()
    print '\nThe Softwares present in the selected project %s are: \n' % (a), softwares
    stdin, stdout, stderr = ssh.exec_command('cd test \n cd software \n cd {0} \n pwd'.format(a))
    pwd = stdout.read()
    pwd = pwd.strip('\n')
    b = raw_input("Select the software you want to download:")

    if b in softwares:
        sftp = ssh.open_sftp()
        remote_file_path = r"{0}/{1}".format(pwd, b)
        sftp.get(remote_file_path, b)
        print "You have successfully downloaded"

    else:
        print "Sorry, the requested software is not present. Please enter your details, will update the inventory"
        user_email = raw_input("Enter your email: ")
        user_pwd = getpass.getpass("Enter your email password:")
        FROM = user_email
        TO = "surya.1510@gmail.com"  # Admin mail remains same in user
        SUBJECT = raw_input("Enter the subject to your email: ")
        def details():
            project_name = raw_input("Enter the Name of the Project: ")
            software = raw_input("Enter the Software to be needed: ")
            return "Needed %s software, under the %s project" %(project_name,software)
            
        TEXT = details()
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("email.nexiilabs.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user_email, user_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print 'Successfully sent the mail'
        except:
            print 'Failed to send mail'

ssh.close()
