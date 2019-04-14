import paramiko
import getpass
from time import sleep

username = raw_input("Enter your username: ")
#Remove below sharp sign to hard code your password
#password = "YOUR PASSWORD HERE"
#use below line to ask for password and echo it to user
#password = raw_input("Enter your password: ")
#use below line to ask for password without echoing it to user
password = getpass.getpass("Enter your password: ")

###########define servers
#use a text file containing your IP addresses (one IP per line)
f = open('.\\IP_List.txt')

for line in f:
    line = line.strip()
    print "connecting to " + (line)
    ip_address = line

#############################
#########SSH client##########
#############################
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=line, username=username, password=password)
    print "Successfully connected to: ", line

    sleep(0.5)
#############################
###########COMMANDS##########
#############################
    remote_connection = ssh_client.invoke_shell()

    sleep(0.1)

    #remote_connection.send("ls -h /etc/cron.d/ | cat > list.txt && cat list.txt\n")
    sleep(0.5)
    remote_connection.send("sudo su\n")
    sleep(0.1)
    remote_connection.send("T0p53CUr!ty\n")
    sleep(0.5)
    remote_connection.send("echo '#!/bin/bash' > script.sh\n")
    remote_connection.send("echo 'echo \"###########HOSTNAME IS:#############\"' >> script.sh\n")
    remote_connection.send("echo 'printenv | grep HOSTNAME=' >> script.sh\n")
    remote_connection.send("echo 'for cronfile in /etc/cron.d/*' >> script.sh\n")
    remote_connection.send("echo do >> script.sh\n")
    #remote_connection.send("echo 'echo \"########FILE NAME IS#########\"' >> script.sh\n")
    #remote_connection.send("echo 'echo \"$cronfile\"' >> script.sh\n")
    remote_connection.send("echo 'echo \"########The FILE Contains:#########\"' >> script.sh\n")
    remote_connection.send("echo cat '$cronfile' >> script.sh\n")
    remote_connection.send("echo done >> script.sh && chmod 777 script.sh\n")
    sleep(0.1)
    remote_connection.send("./script.sh > cron-files.txt\n")
    sleep(0.1)
    remote_connection.send("cat cron-files.txt\n")
    remote_connection.send("mkdir /mnt/smb\n")
    remote_connection.send("mount //10.254.2.30/cronfiles/ /mnt/smb -o user=y.khodadadi \n")
    sleep(0.1)
    remote_connection.send("T0p53CUr!ty\n")
    sleep(0.2)
    remote_connection.send("cp cron-files.txt/mnt/smb/$HOSTNAME-Cron-Summary.txt\n")
    sleep(0.1)
    remote_connection.send("umount /mnt/smb\n")
    remote_connection.send("rm -rf script.sh\n")
    remote_connection.send("rm -rf cron-files.txt\n")
    remote_connection.send("rm -rf /mnt/smb\n")
    #remote_connection.send("rm -rf cron-files.txt\n")

###########print output

    sleep(0.1)
    output = remote_connection.recv(65535)
    print output

###########closing session
    ssh_client.close()

f.close()

exit()
