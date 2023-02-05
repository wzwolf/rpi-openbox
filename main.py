#! /usr/bin/env python3

import os
import subprocess
import sys
import re
import time

# declare var
address = "/usr/bin/startlxde-pi"

# declare functions
def checkforillegalchars(inputstring):
    """return true if inputstring include illegal char -input error
    return false if inputstring does not include illegal char - pass"""
    if re.search(r"[ ,!@#$%^&+=?<>/()*~:;`\{\}\[\]\|\"\'\-]",inputstring) != None:
        return True #input error
    return False # pass

def checkforYesOrNo(inputstring):
    """return true if inputstring does not include yes or no - input error
    return false if inputstring contain yes or no - pass"""
    if re.search(r"[Yy][Ee][Ss]|[Nn][Oo]|[Yy]|[Nn]",inputstring) == None:
        return True # input error
    return False # pass

def checkforYes(inputstring):
    """return true if inputstring include yes
    return false if inputstring does not contain yes """
    if re.search(r"[Yy][Ee][Ss]|[Yy]",inputstring) == None:
        return True # input error
    return False # pass

#check if file exist, if not exit program
if os.path.isfile(address) == False:
    print("file @ " + address +" does not exist" )
    sys.exit(1)

# modify file
searchexp = "2048"
replaceexp = "22480"
sedcmd = "s/"+searchexp+"/"+replaceexp +"/g"
modifyfile = subprocess.run(["sudo","sed","-i",sedcmd,address])
if modifyfile.returncode != 0:
    print("unable to edit file. abort")
    sys.exit(1)
else:
    # file is modified
    # check if want to reboot to initate changes
    print(os.getcwd())
    checkreboot = input("Do you want to reboot computer?:")
    while(checkforillegalchars(checkreboot) or checkforYesOrNo(checkreboot)):
        # ask user again for input due to input error
        checkreboot = input("please reply yes or no")
    if checkforYes:
        print("rebooting Now")
        # wait 5 secs
        time.sleep(5)
        rebootprocess = subprocess.run(["sudo","reboot"])
        if rebootprocess.returncode != 0:
            print("unable to reboot. abort")
            sys.exit(1)
    else:
        print("System not rebooted. reboot at your own convenience")
        sys.exit(0)
