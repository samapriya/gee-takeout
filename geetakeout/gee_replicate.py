import requests,json,re,csv,os,subprocess,urllib2
from pprint import pprint
from os.path import expanduser
from urllib2 import Request, urlopen
import dateutil.parser as parser
import ee
ee.Initialize()

def replicate(idl):
    with open(idl,'r') as f:
        reader = csv.DictReader(f)
        for i, line in enumerate(reader):
            destype = line['type']
            source = line['path']
            dest_root = str(ee.data.getAssetRoots()[0]['id'])
            sourc_root="users/"+source.split('/')[1]
            print("Destination Source: "+dest_root,"Source root: "+sourc_root)
            destination=source.replace(sourc_root,dest_root)
            print("Final Destination: "+destination)
            print('')
            if destype== "Folder" and ee.data.getInfo(destination) is not None:
                print("Folder Exists")
            elif destype== "Folder" and ee.data.getInfo(destination) is None:
                folder=dest_root+'/'+str(source.replace(sourc_root,'')).split('/')[-1]
                print(folder)
                ee.data.createAsset({'type': ee.data.ASSET_TYPE_FOLDER}, folder)
            elif destype=="ImageCollection" and ee.data.getInfo(destination) is not None:
                print('ImageCollection Exists')
            elif destype=="ImageCollection" and ee.data.getInfo(destination) is None:
                folder=str(source.replace(sourc_root,'')).split('/')[-1]
                ee.data.createAsset({'type': ee.data.ASSET_TYPE_IMAGE_COLL}, destination)
#replicate(idl=r'C:\Users\samapriya\Desktop\gee-copy\eerep.csv')
