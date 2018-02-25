import os,subprocess,csv
from pprint import pprint
from os.path import expanduser
from urllib2 import Request, urlopen
import dateutil.parser as parser
import ee
ee.Initialize()

def permission(idl,user):
    with open(idl,'r') as f:
        reader = csv.DictReader(f)
        for i, line in enumerate(reader):
            mode = line['type']
            asset = line['path']
            ## Reads the IDL files and categorizes it to give permission            
            if mode=='Folder':
                try:
                    for line in subprocess.check_output("earthengine ls"+" "+asset).split('\n'):
                        asst=line
                        print(asst)
                        asset_acl=subprocess.check_output("earthengine acl ch "+asst+" -u"+" "+user)
                        print(ee.data.getAssetAcl(asst))
                except Exception:
                    print("Permissions Error Check Again")
            elif mode=='ImageCollection':
                try:
                    asset_acl=subprocess.check_output("earthengine acl ch "+asset+" "+" -u"+" "+user)
                    print(asset)
                    print(ee.data.getAssetAcl(asset))
                    print("Permissions Changed")
                except Exception:
                    print("Permissions Error Check Again")
            elif mode=='Image':
                try:
                    asset_acl=subprocess.check_output("earthengine acl ch "+asset+" "+" -u"+" "+user)
                    print(asset)
                    print(ee.data.getAssetAcl(asset))
                    print("Permissions Changed")
                except Exception:
                    print("Permissions Error Check Again")
            elif mode=='Table':
                try:
                    asset_acl=subprocess.check_output("earthengine acl ch "+asset+" "+" -u"+" "+user)
                    print(asset)
                    print(ee.data.getAssetAcl(asset))
                    print("Permissions Changed")
                except Exception:
                    print("Permissions Error Check Again")

#permission(idl=r'C:\Users\samapriya\Desktop\gee-copy\eerep.csv',user="roysam@iu.edu:R")
