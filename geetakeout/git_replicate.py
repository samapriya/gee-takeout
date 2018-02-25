import os
import subprocess
import sys
'''
Use tool with caution:
Create a new repo first which is your remote directory only write to an empty directory
Download git first
Then go to https://earthengine.googlesource.com and click on generate password and follow instructions
Once your git bash is registered to the google account you will be able to pull or push to it
Local directory points to the git directory downloaded from a different account the account you want to replicate
Once push command is issued you cannot go back to any history and will loose all code if the remote repo was not empty
'''

def geerep(local,remote):
    for items in os.listdir(local):
        try:
            if items.endswith(".git"):
                os.system('rmdir '+'"'+os.path.join(local,items)+'" /s /q')
            else:
                pass
        except Exception as e:
            print(e)
    os.chdir(local)
    try:
        subprocess.check_output("git init")
    except Exception:
        print(e)
        sys.exit()
    try:
        subprocess.check_output("git add .")
    except Exception as e:
        print(e)
        sys.exit()
    try:
        subprocess.check_output("git commit -m 'replicate' ")
    except Exception as e:
        print(e)
        sys.exit()
    try:
        subprocess.check_output("git remote add origin "+remote)
    except Exception as e:
        print(e)
        sys.exit()
    try:
        subprocess.check_output("git remote -v")
    except Exception as e:
        print(e)
        sys.exit()
    try:
        subprocess.check_output("git push origin master --force")
    except Exception as e:
        print(e)
        sys.exit()
##geerep(local=r"C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Earth Engine Codes\EE_Replicate\Code Replication\Code-Downloader\sam",
##       remote="https://earthengine.googlesource.com/users/roysam-io/avulsion")

def geerep_rec(folder,root):
    for itms in os.listdir(folder):
        local=os.path.join(folder,itms)
        remote=str(os.path.join("https://earthengine.googlesource.com/users",root,itms)).replace("\\",'/')
        print("Now moving "+str(local))
        geerep(local=local,remote=remote)
        
#geerep_rec(folder=r"C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Earth Engine Codes\EE_Replicate\Code Replication\Code-Downloader\gitee-cli\samapriya",
#           root="extasset")
    
