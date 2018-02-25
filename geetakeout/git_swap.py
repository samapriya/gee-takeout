import os
def gitswap(gitkey):
    with open(gitkey,'r') as f:
        item=f.read().split('\n')
        for k,items in enumerate(item):
            os.system(items)
#gitswap(gitkey=r"C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Earth Engine Codes\EE_Replicate\Code Replication\Code-Downloader\git-pass\git-samapriya")
