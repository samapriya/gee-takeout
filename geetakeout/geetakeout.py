#! /usr/bin/env python

import argparse
import os,platform
import ee
import subprocess
import getpass
import csv
from ee import oauth
import re
import time
import clipboard
import shutil
from datetime import date, timedelta
from os.path import expanduser
from git_geerepolist import gee_repo
from git_password import gitwinauth
from git_swap import gitswap
from git_copy import gitclone
from git_repocreate import gitcreate_rec
from git_replicate import geerep_rec
from gee_report import ee_report
from gee_permissions import permission
from gee_replicate import replicate
from gee_assetcopy import assetcopy
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,os,subprocess,ee,getpass
from ee import oauth
os.chdir(os.path.dirname(os.path.realpath(__file__)))
gee_home = expanduser("~/.config/earthengine/")
pathway=os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(expanduser("~"),"eecred")):
    os.makedirs(os.path.join(expanduser("~"),"eecred"))
user_home = expanduser("~")
gtakehome=expanduser("~/geetakeout")
if not os.path.exists(os.path.join(expanduser("~"),"geetakeout")):
    os.makedirs(os.path.join(expanduser("~"),"geetakeout"))
#Earth Engine tools
#Update drivers
def update():
    if str(platform.system()) =="Windows":
        os.system("python sel-latest-win.py")
        print("Updated selenium driver for Windows64")
    elif str(platform.system()) =="Linux":
        os.system("python sel-latest-linux.py")
        print("Updated selenium driver for Linux64")
    else:
        print("Architecture not recognized")
def update_from_parser(args):
    update()

##Create and Save Earth Engine Credentials (allows user to make a copy of the credential file)
def ee_user_from_parser(args):
    folder=os.path.join(expanduser("~"),"eecred")
    try:
        auth_url = ee.oauth.get_authorization_url()
        clipboard.copy(auth_url)
        print("Authentication link copied: Go to browser and click paste and go")
        time.sleep(10)
        print("Enter your GEE API Token")
        password=str(getpass.getpass())
        auth_code=str(password)
        token = ee.oauth.request_token(auth_code)
        ee.oauth.write_token(token)
        print('\nSuccessfully saved authorization token.')
        rootdir=str(subprocess.check_output("earthengine ls",shell=False))
        print("Your root directory is ")
        print(rootdir)
    except Exception as e:
        #print(e)
        pass

#Download the Git Repo List Easier to Parse once downloaded and allows you to push you others too
def gee_repo_from_parser(args):
    gee_repo()

#Downloads and saves your
def gitwinauth_from_parser(args):
    '''This allows you to create the ee git keys necessary to authorize source account'''
    gitwinauth()

#This allows you to replace the git keys
def gitswap_from_parser(args):
    gitswap(gitkey=args.gitkey)

#This actually downloads all your repositories
def gitclone_from_parser(args):
    gitclone()

#This allows you to recreate the repo structure
def gitcreate_rec_from_parser(args):
    gitcreate_rec(folder=args.folder)

#Make sure you use gitwinauth again to change authentication of your system git to new account
def geerep_rec_from_parser(args):
    geerep_rec(folder=args.folder,root=args.root)


##Now we look into how to replicate data structure##

#Generate report from the account you want to copy
def ee_report_from_parser(args):
    ee_report(output=args.output)

#Make sure you use gitwinauth again to change authentication of your system git to new account
def permission_from_parser(args):
    permission(idl=args.input,user=args.upermission)

#Now to make sure the home folder structure in the second account ia matched
def replicate_from_parser(args):
    replicate(idl=args.report)

#Last step copies all assets from source account to destination
def assetcopy_from_parser(args):
    assetcopy(idl=args.report)
spacing="                               "

def main(args=None):
    parser = argparse.ArgumentParser(description='Command line tool to copy Google Earth Engine Codes and assets from one account to another\n'
                                                 '------------------------------------------------------------'
                                                 '--------------\n'
                                                 'https://github.com/samapriya/gee-takeout')
    subparsers = parser.add_subparsers()
    parser_EE00 = subparsers.add_parser(' ', help='.\n')
    parser_EE01 = subparsers.add_parser(' ', help='---------EE Setup and Housekeeping---------')
    parser_EE02 = subparsers.add_parser(' ', help='.\n')

    parser_update=subparsers.add_parser('update',help='Updates Selenium drivers for firefox[Tested on Win-10 and Ubuntu-16]')
    parser_update.set_defaults(func=update_from_parser)

    parser_ee_user = subparsers.add_parser('ee_user', help='Get Earth Engine API Key & Paste it back to Command line/shell to change user')
    parser_ee_user.set_defaults(func=ee_user_from_parser)

    parser_EE1 = subparsers.add_parser(' ', help='.\n')
    parser_EE = subparsers.add_parser(' ', help='-----------Setup the first account----------')
    parser_EE2 = subparsers.add_parser(' ', help='.\n')

    parser_gee_repo=subparsers.add_parser('gee_repo',help='Downloads your GEE Repo List including others in Global Access')
    parser_gee_repo.set_defaults(func=gee_repo_from_parser)

    parser_gitwinauth=subparsers.add_parser('git_auth',help='This allows you to access your GEE github and validate that you are setup to clone from directory')
    parser_gitwinauth.set_defaults(func=gitwinauth_from_parser)

    parser_gitswap=subparsers.add_parser('git_swap',help='This allows access your stored git password and validate that you are setup to clone from directory')
    parser_gitswap.add_argument('--gitkey', help='Path to the git authorization key you saved earlier in the same folder as this tool', required=True)
    parser_gitswap.set_defaults(func=gitswap_from_parser)

    parser_gitclone=subparsers.add_parser('git_clone',help='This clones folder based on your root directory(your root directory can be found using earthengine ls)')
    parser_gitclone.set_defaults(func=gitclone_from_parser)

# This is the point at which we start we start to work on assets
    parser_ee_report=subparsers.add_parser('ee_report',help='This looks at the primary account from which you are copying assets & generates a report')
    parser_ee_report.add_argument('--output', help='Full path to a csv file where the report will be saved', required=True)
    parser_ee_report.set_defaults(func=ee_report_from_parser)

    parser_permission=subparsers.add_parser('ee_permissions',help='This allows you to set permissions for the second account, a read or R permission is sufficient')
    parser_permission.add_argument('--input', help='This is the input report file you generated in the earlier step', required=True)
    parser_permission.add_argument('--upermission', help='This is the permission dictionary in the setup "abc@gmail.com:R"', required=True)
    parser_permission.set_defaults(func=permission_from_parser)


# This is the point at which we start working on the second account
    parser_EE3 = subparsers.add_parser(' ', help='.\n')
    parser_EE4 = subparsers.add_parser(' ', help='------Change to second account use git_auth and git_swap to change account------')
    parser_EE5 = subparsers.add_parser(' ', help='.\n')

    parser_gitcreate=subparsers.add_parser('git_create',help='This allows you to replicate the repository structure in destination EE account')
    parser_gitcreate.add_argument('--folder', help='Folder where you cloned all repos to be replicated', required=True)
    parser_gitcreate.set_defaults(func=gitcreate_rec_from_parser)

    parser_geerep_rec=subparsers.add_parser('git_replicate',help='This allows you to access your GEE github in your destination account and transfer codes')
    parser_geerep_rec.add_argument('--folder', help='Folder where you cloned all repos to be replicated', required=True)
    parser_geerep_rec.add_argument('--root', help='This is the root path to the new account the part after users/', required=True)
    parser_geerep_rec.set_defaults(func=geerep_rec_from_parser)

# This is the point at which we start we start to work on assets
    parser_replicate=subparsers.add_parser('asset_create',help='This tool replicates the home folder structure and creates empty folder and collections')
    parser_replicate.add_argument('--report', help='Full path to a csv file to the EE report created earlier', required=True)
    parser_replicate.set_defaults(func=replicate_from_parser)

    parser_assetcopy=subparsers.add_parser('asset_replicate',help='This now copies all assets images, tables and collections to the home folder in the second account')
    parser_assetcopy.add_argument('--report', help='Full path to a csv file to the EE report created earlier', required=True)
    parser_assetcopy.set_defaults(func=assetcopy_from_parser)

    args = parser.parse_args()
    ee.Initialize()
    args.func(args)

if __name__ == '__main__':
    main()
