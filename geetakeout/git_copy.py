import os
import shutil
import time
import subprocess
from os.path import expanduser
from bs4 import BeautifulSoup
local=os.path.dirname(os.path.realpath(__file__))
gtakehome=expanduser("~/geetakeout")
if not os.path.exists(os.path.join(expanduser("~"),"geetakeout")):
    os.makedirs(os.path.join(expanduser("~"),"geetakeout"))
def gitclone():
    user=str(subprocess.check_output("earthengine ls")).split("/")[-1].strip()
    print(user)
    try:
        filename=os.path.join(local,"eed-users.html")
        with open(filename,"r") as html_file:
            soup=BeautifulSoup(html_file,'lxml')

        for article in soup.find_all(class_='RepoList-item'):
            if user in article.text:
                ldirc=os.path.join(gtakehome,user)
                dirc=os.path.join(ldirc,str(article.text).split("/")[-1])
                print(ldirc,dirc)
                if not os.path.exists(ldirc):
                    os.makedirs(ldirc)
                    os.chdir(ldirc)
                    try:
                        os.system("git clone https://earthengine.googlesource.com/users/"+str(article.text))
                        print("Cloning "+str(article.text)+" to "+str(os.getcwd()))
                    except Exception as e:
                        print(e)
                else:
                    os.system('rmdir '+'"'+dirc+'" /s /q')
                    os.chdir(ldirc)
                    try:
                        os.system("git clone https://earthengine.googlesource.com/users/"+str(article.text))
                        print("Cloning "+str(article.text)+" to "+str(os.getcwd()))
                    except Exception as e:
                        print(e)
                try:
                    for dirname, subdirs,filelist in os.walk(ldirc):
                        if dirname.endswith(".git"):
                            os.system('rmdir '+'"'+dirname+'" /s /q')
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
    print("Git repos are saved in "+str(gtakehome))
#gitclone()
