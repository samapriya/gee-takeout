from __future__ import print_function
import ee,json,csv,subprocess
ee.Initialize()
def ee_report(output):
    with open(output,"wb") as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=["type", "path"], delimiter=',')
        writer.writeheader()
    a=subprocess.check_output("earthengine ls")
    b=subprocess.check_output("earthengine ls "+a+" -l -r")
    try:
        for item in b.split('\n'):
            a=item.replace("[","").replace("]","").split()
            header=a[0]
            tail=a[1]
            if header=="ImageCollection":
                print(tail)
                with open(output,"a") as csvfile:
                    writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                    writer.writerow([header,tail])
                csvfile.close()
            elif header=="Image":
                with open(output,"a") as csvfile:
                    writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                    writer.writerow([header,tail])
                csvfile.close()
            elif header=="Table":
                with open(output,"a") as csvfile:
                    writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                    writer.writerow([header,tail])
                csvfile.close()
            elif header=="Folder": ##Folders are not added to the list but are print
                with open(output,"a") as csvfile:
                    writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                    writer.writerow([header,tail])
                csvfile.close()
                print("Folder "+str(tail))
    except Exception as e:
        return "worked"
#ee_report(output=r"C:\Users\samapriya\Desktop\eerep.csv")
