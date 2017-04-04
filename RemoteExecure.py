#!/usr/bin/env python
##                                            											##
##                                            											##
##                                            											##
##                                            											##
##    User Create on Remote Machine and Send a Mail on the Successfull Status       	##
##                                            											##
##                                            											##
##                                            						28/Feb/2017	babith.g	##

import subprocess
import sys
import crypt
import logging
import logging.handlers
import random
import string
from random import randint


LOG_FILENAME = 'Remote_User_Add.log'
Host_list = ""
Host = ""
password = ''.join(random.choice(string.ascii_lowercase+string.digits) for _  in range(8))
encPass = crypt.crypt(password,str(randint(10,20)))
username = ""
name = ""
userid = ""
pri_group = ""
sec_group = ""
COMMAND = ""

# This details are related to the logging 
result_logger = logging.getLogger("Result_Logging")
result_logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
#result_logger_ch = logging.StreamHandler()
result_logger_ch = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1860,backupCount=5)
result_logger_ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to result_logger_ch
result_logger_ch.setFormatter(formatter)

# add result_logger_ch to logger
result_logger.addHandler(result_logger_ch)


def helpit():
    print("Error: Program require all the fields while running ")
    print("""
        Syntax:
        RemoteExecure.py Name UserName UserID Primary_GroupID Secondary_GroupID ServerListFile UserEmailID

        Name           - Name of the user with out white space Underscore can use eg: John_Smith
        UserName      - Name Which user will be login it should be lowercase letters eg: johns
        UserID          - Unique User number eg:1001
        Primary_GroupID      - Primary Group of the user 
        Secondary_GroupID - Secondary Groups of the user give the list with comma eg:10,12
        ServerListFile      - File contains the list of servers which the user needs to be created
        UserEmailID      - Mail Id of the user so that finally inform the user 
         """)
    exit()


def remote_useradd(HOST):
        ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
    error_check = ssh.stderr.readlines()
        if error_check <> []:
                return ", Error: " , result_logger.warning(' Server: {:10} - User ID: "{:10}" - error exiting from remote_useradd()'.format(Host,username))
        else:
                return ", Successfull: ", result_logger.info('    Server: {:10} - User ID: "{:10}" - created Successfully with - UID: {:5}'.format(Host,username,userid))


# Program Begines here

if len(sys.argv) <> 8:
    helpit()
else:
    name = sys.argv[1]
    username = sys.argv[2]
    userid = sys.argv[3]
    pri_group = sys.argv[4]
    sec_group = sys.argv[5]
    server_file = open(sys.argv[6], 'r')
    Host_list = map(lambda one:one.strip('\n'),server_file.readlines())
    server_file.close()
    usermail_id = sys.argv[7]
    COMMAND = "useradd -p "+encPass+" -s /bin/bash -u "+userid+" -g "+pri_group+" -G "+sec_group+" -d /home/"+username+ " -m -c \""+name+"\" " + username
    print(COMMAND)
    # Executing the command on all the listed servers
    for Host in Host_list:
        print ('\nServer Name : {} User ID: {}'.format(Host,username))
        remote_useradd(Host)

#subprocess.call(['ls', '-ltr', sys.argv[6]])
cat filename | sendmail -s "User created" mailid

print("[+] done '"+password+"'")
