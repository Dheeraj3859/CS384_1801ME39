import csv
import os

path="/home/manunem3859/Desktop/lab_personal/Assignment3/analytics"
print(os.getcwd())

def course():
    # Read csv and process
    fieldnames=['id','full_name','country','email','gender','dob','blood_group','state']
    branch_code=["CS","EE","ME","CB","CE","MC","MS","MT","NT","CH","HS","MA","PH"]
    stream_code=["01","11","12","21"]
    year_code=["15","16","17","18","19"]
    
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            roll=row['id']
            bc=roll[4:6]
            sc=roll[2:4]
            yc=roll[0:2]
            
            if bc in branch_code and sc in stream_code and yc in year_code:
                if bc=="CS":
                    direc="cs"
                    path1=os.path.join(path,'course',direc)
                    #if os.path.exists(path1)==False:
                        #os.mkdir(path1)
                    if sc=="01":
                        direc1='btech'
                        path2=os.path.join(path1,direc1)
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        #path2=os.path.join(path2,'btech')
                        #os.mkdir(path2)p
                        
                        if yc=="15":
                            with open(os.path.join(path2,'15_cs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','cs','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','cs','mtech')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','cs','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)






            else:
                path3=os.path.join(path,'course')

                with open(os.path.join(path3,'misc.csv'),'a') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
                

course()


    
"""
def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
"""