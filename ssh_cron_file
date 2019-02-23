import paramiko
import getpass
from time import sleep

###########define servers
ip_address = "IP_ADDRESS"
username = raw_input("Enter your username: ")
#password = getpass.getpass()
#password = "PASSWORD"
#p = getpass.getpass(prompt='What is your favorite color? ')
#############################
#########SSH client##########
#############################
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=getpass.getpass())
print "Successfully connected to: ", ip_address

sleep(0.5)
#############################
###########COMMANDS##########
#############################
remote_connection = ssh_client.invoke_shell()

sleep(0.1)

#remote_connection.send("ls -h /etc/cron.d/ | cat > list.txt && cat list.txt\n")
sleep(0.5)
remote_connection.send("echo '#!/bin/bash' > script.sh\n")
remote_connection.send("echo 'echo \"###########HOSTNAME IS:#############\"' >> script.sh\n")
remote_connection.send("echo 'printenv | grep HOSTNAME=' >> script.sh\n")
remote_connection.send("echo 'for cronfile in /etc/cron.d/*' >> script.sh\n")
remote_connection.send("echo do >> script.sh\n")
remote_connection.send("echo 'echo \"########FILE NAME IS#########\"' >> script.sh\n")
remote_connection.send("echo 'echo \"$cronfile\"' >> script.sh\n")
remote_connection.send("echo 'echo \"########The FILE Contains:#########\"' >> script.sh\n")
remote_connection.s end("echo cat '$cronfile' >> script.sh\n")
remote_connection.send("echo done >> script.sh && chmod 777 script.sh\n")
sleep(0.1)
remote_connection.send("./script.sh > cron-files.txt\n")
sleep(0.1)
#remote_connection.send("rm -rf script.sh\n")


###########print output
sleep(0.1)
output = remote_connection.recv(65535)
print output

###########closing session
ssh_client.close()

exit()
