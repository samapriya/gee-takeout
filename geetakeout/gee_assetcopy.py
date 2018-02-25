#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import ee
ee.Initialize()


def assetcopy(idl):
    with open(idl, 'r') as f:
        reader = csv.DictReader(f)
        for (i, line) in enumerate(reader):
            destype = line['type']
            source = line['path']
            if destype == 'Image':
                source = line['path']
                dest_root = str(ee.data.getAssetRoots()[0]['id'])
                sourc_root = 'users/' + source.split('/')[1]
                destination = source.replace(sourc_root, dest_root)
                print 'Transfering to Image ' + str(destination)
                try:
                    if ee.data.getInfo(destination) is None:
                        ee.data.copyAsset(source, destination)
                    else:
                        pass
                except Exception, e:

                        # print("Skipping image already exists")

                    print e
            elif destype == 'Table':
                source = line['path']
                dest_root = str(ee.data.getAssetRoots()[0]['id'])
                sourc_root = 'users/' + source.split('/')[1]
                destination = source.replace(sourc_root, dest_root)
                print 'Transfering to Table ' + str(destination)
                try:
                    if ee.data.getInfo(destination) is None:
                        ee.data.copyAsset(source, destination)
                    else:
                        pass
                except Exception, e:

                        # print("Skipping image already exists")

                    print e
            elif destype == 'ImageCollection':
                source = line['path']
                sourcesize = ee.ImageCollection(source).size().getInfo()
                dest_root = str(ee.data.getAssetRoots()[0]['id'])
                sourc_root = 'users/' + source.split('/')[1]
                destination = source.replace(sourc_root, dest_root)
                print 'Transfering to ImageCollection ' \
                    + str(destination)
                list_req = {'id': source}
                children = ee.data.getList(list_req)
                for items in children:
                    img = str(items['id'])
                    dest = str(items['id']).replace(sourc_root,
                            dest_root)
                    try:
                        if ee.data.getInfo(dest) is None:
                            ee.data.copyAsset(img, dest)
                            destinationsize = \
                                ee.ImageCollection(destination).size().getInfo()
                            print 'Remaining items ' \
                                + str(int(sourcesize)
                                    - int(destinationsize))
                        else:
                            pass
                    except Exception, e:

                            # print("Skipping image already exists")

                        print e


#assetcopy(idl=r'C:\Users\samapriya\Desktop\eerep2.csv')
