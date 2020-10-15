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

                if bc=="EE":
                    direc="ee"
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
                            with open(os.path.join(path2,'15_ee_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ee_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ee_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ee_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ee_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ee','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ee_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ee_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ee_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ee_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ee_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ee','mtech')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ee_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ee_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ee_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ee_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ee_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ee','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ee_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ee_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ee_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ee_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ee_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst) 

                if bc=="ME":
                    direc="me"
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
                            with open(os.path.join(path2,'15_me_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_me_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_me_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_me_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_me_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','me','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_me_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_me_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_me_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_me_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_me_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','me','mtech')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_me_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_me_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_me_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_me_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_me_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','me','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_me_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_me_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_me_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_me_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_me_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="CE":
                    direc="ce"
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
                            with open(os.path.join(path2,'15_ce_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ce_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ce_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ce_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ce_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ce','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ce_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ce_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ce_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ce_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ce_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ce','mtech')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ce_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ce_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ce_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ce_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ce_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ce','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ce_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ce_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ce_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ce_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ce_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="CB":
                    direc="cb"
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
                            with open(os.path.join(path2,'15_cb_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cb_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cb_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cb_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cb_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','cb','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cb_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cb_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cb_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cb_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cb_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','cb','mtech')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cb_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cb_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cb_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cb_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cb_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','cb','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_cb_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_cb_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_cb_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_cb_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_cb_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="MC":
                    direc="mc"
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
                            with open(os.path.join(path2,'15_mc_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mc_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mc_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mc_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mc_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','mc','msc')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mc_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mc_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mc_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mc_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mc_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','mc','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mc_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mc_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mc_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mc_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mc_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','mc','phd')
                        if os.path.exists(path2)==False:
                            os.mkdir(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mc_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mc_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mc_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mc_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mc_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="MS":
                    direc="ms"
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
                            with open(os.path.join(path2,'15_ms_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ms_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ms_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ms_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ms_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ms','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ms_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ms_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ms_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ms_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ms_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ms','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ms_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ms_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ms_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ms_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ms_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ms','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ms_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ms_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ms_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ms_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ms_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="MT":
                    direc="mt"
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
                            with open(os.path.join(path2,'15_mt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','mt','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','mt','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','mt','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_mt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_mt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_mt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_mt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_mt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="NT":
                    direc="nt"
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
                            with open(os.path.join(path2,'15_nt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_nt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_nt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_nt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_nt_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','nt','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_nt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_nt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_nt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_nt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_nt_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','nt','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_nt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_nt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_nt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_nt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_nt_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','nt','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_nt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_nt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_nt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_nt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_nt_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="CH":
                    direc="ch"
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
                            with open(os.path.join(path2,'15_ch_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ch_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ch_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ch_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ch_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ch','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ch_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ch_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ch_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ch_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ch_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ch','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ch_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ch_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ch_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ch_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ch_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ch','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ch_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ch_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ch_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ch_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ch_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="HS":
                    direc="hs"
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
                            with open(os.path.join(path2,'15_hs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_hs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_hs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_hs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_hs_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','hs','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_hs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_hs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_hs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_hs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_hs_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','hs','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_hs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_hs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_hs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_hs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_hs_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','hs','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_hs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_hs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_hs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_hs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_hs_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="MA":
                    direc="ma"
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
                            with open(os.path.join(path2,'15_ma_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ma_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ma_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ma_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ma_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ma','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ma_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ma_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ma_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ma_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ma_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ma','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ma_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ma_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ma_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ma_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ma_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ma','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ma_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ma_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ma_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ma_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ma_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                if bc=="PH":
                    direc="ph"
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
                            with open(os.path.join(path2,'15_ph_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ph_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ph_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ph_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ph_btech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="12":
                        
                        path2=os.path.join(path,'course','ph','msc')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ph_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ph_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ph_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ph_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ph_msc.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                    if sc=="11":
                        path2=os.path.join(path,'course','ph','mtech')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ph_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ph_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ph_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ph_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ph_mtech.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)

                    if sc=="21":
                        path2=os.path.join(path,'course','ph','phd')
                        if os.path.exists(path2)==False:
                            os.makedirs(path2)
                        if yc=="15":
                            with open(os.path.join(path2,'15_ph_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="16":
                            with open(os.path.join(path2,'16_ph_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="17":
                            with open(os.path.join(path2,'17_ph_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="18":
                            with open(os.path.join(path2,'18_ph_phd.csv'),'a+') as fi:
                                csvwriter=csv.writer(fi)
                                lst=[]
                                for keys in row:
                                    lst.append(row[keys])
                                csvwriter.writerow(lst)
                        if yc=="19":
                            with open(os.path.join(path2,'19_ph_phd.csv'),'a+') as fi:
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
                

#course()


    

def country():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            Country=row['country']
            path1=os.path.join(path,'country')
            file_name=Country+'.csv'
            if os.path.exists(os.path.join(path1,file_name))==True:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writeheader(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)

            

#country()


def fun(st):
    i=0
    for c in st:
        if c=='@':
            i+=1
            break
        else:
            i+=1
    str=""
    while st[i]!='.':
        str+=st[i]
        i+=1
    return str

        

def email_domain_extract():
    # Read csv and process
    temp=os.path.join(path,'email_domain')
    if os.path.exists(temp)==False:
        os.mkdir(temp)
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            s=row['email']
            domain=fun(s)
            path1=os.path.join(path,'email_domain')
            file_name=domain+'.csv'
            if os.path.exists(os.path.join(path1,file_name))==True:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)


            
#email_domain_extract()

def gender():
    # Read csv and process
    temp=os.path.join(path,'gender')
    if os.path.exists(temp)==False:
        os.mkdir(temp)
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            gend=row['gender']
            path1=os.path.join(path,'gender')
            file_name=gend+'.csv'
            if os.path.exists(os.path.join(path1,file_name))==True:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
    
#gender()

def dob():
    # Read csv and process
    temp=os.path.join(path,'dob')
    if os.path.exists(temp)==False:
        os.mkdir(temp)
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            strin=row['dob']
            li=strin.split('-')
            birth_year=int(li[2])
            file_name=""
            if birth_year>=1995 and birth_year<=1999:
                file_name+="bday_1995_1999.csv"
            elif birth_year>=2000 and birth_year<=2004:
                file_name+="bday_2000_2004.csv"
            elif birth_year>=2005 and birth_year<=2009:
                file_name+="bday_2005_2009.csv"
            elif birth_year>=2010 and birth_year<=2014:
                file_name+="bday_2010_2014.csv"
            elif birth_year>=2015 and birth_year<=2020:
                file_name+="bday_2015_2020.csv"
            path1=os.path.join(path,'dob')
            if os.path.exists(os.path.join(path1,file_name))==True:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)

#dob()  


def state():
    # Read csv and process
    temp=os.path.join(path,'state')
    if os.path.exists(temp)==False:
        os.mkdir(temp)
    with open('studentinfo_cs384.csv') as file:
        reader=csv.DictReader(file)
        for row in reader:
            sta=row['state']
            path1=os.path.join(path,'state')
            file_name=sta+'.csv'
            if os.path.exists(os.path.join(path1,file_name))==True:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)


#state()


    


def blood_group():
    # Read csv and process
    temp=os.path.join(path,'blood_group')
    if os.path.exists(temp)==False:
        os.mkdir(temp)
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            bg=row['blood_group']
            path1=os.path.join(path,'blood_group')
            file_name=bg+'.csv'
            if os.path.exists(os.path.join(path1,file_name)):
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path1,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                    lst=[]
                    for keys in row:
                        lst.append(row[keys])
                    csvwriter.writerow(lst)


    

blood_group()
# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
