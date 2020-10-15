import csv
import os
import operator
import shutil
import re
path="/home/manunem3859/Desktop/lab_personal/Assignment3/analytics"

def getString(x):
    if x=="01":
        return 'btech'
    elif x=="11":
        return 'mtech'
    elif x=="12":
        return 'msc'
    elif x=="21":
        return 'phd'

def del_create_analytics_folder():
    # del the analytics folder including subfolder

    if os.path.exists(path)==True:
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
    # mkdir the analytics folder (only mkdir)


def course():
    fieldnames=['id','full_name','country','email','gender','dob','blood_group','state']
    #branch_code=["CS","EE","ME","CB","CE","MC","MS","MT","NT","CH","HS","MA","PH"]
    stream_code=["01","11","12","21"]
    year_code=["15","16","17","18","19"]
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            roll=row['id']
            bc=roll[4:6].lower()
            sc=roll[2:4]
            yc=roll[0:2]
            if sc in stream_code and yc in year_code and len(roll)==8:
                file_name=yc+"_"+bc+"_"+getString(sc)+".csv"
                path1=os.path.join(path,'course',bc,getString(sc))
                if os.path.exists(path1)==False:
                    os.makedirs(path1)
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
            else:
                path3=os.path.join(path,'course')
                if os.path.exists(path3)==False:
                    os.mkdir(path3)
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
            if os.path.exists(path1)==False:
                os.mkdir(path1)
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
                    csvwriter.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
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


#blood_group()
# Create the new file here and also sort it in this function only.
def fun1():
    with open('studentinfo_cs384_names_split.csv') as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(row)


def new_file_sort():
    # Read csv and process
    new_field_names=['id','first_name','last_name','country','email','gender','dob','blood_group','state']
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.DictReader(file)
        file_name="studentinfo_cs384_names_split.csv"
        for row in reader:
            Name=row['full_name'].split(' ')
            
            if os.path.exists(os.path.join(path,file_name))==True:
                with open(os.path.join(path,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    lst=[]
                    lst.append(row['id'])
                    lst.append(Name[0])
                    tem=""
                    for k in range(1,len(Name)):
                        tem+=Name[k]
                    lst.append(tem)
                    for i in range(3,len(new_field_names)):
                        lst.append(row[new_field_names[i]])
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path,file_name),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(new_field_names)
                    lst=[]
                    lst.append(row['id'])
                    lst.append(Name[0])
                    tem=""
                    for k in range(1,len(Name)):
                        tem+=Name[k]
                    lst.append(tem)
                    for i in range(3,len(new_field_names)):
                        lst.append(row[new_field_names[i]])
                    csvwriter.writerow(lst)


    with open(os.path.join(path,file_name),'r') as file1:
        reader1=csv.DictReader(file1)
        file_name2='studentinfo_cs384_names_split_sorted_first_name.csv'
        new_sorted_list=sorted(reader1,key=operator.itemgetter('first_name'))
        for row in new_sorted_list:
            lst=row.values()
            if os.path.exists(os.path.join(path,file_name2))==True:
                with open(os.path.join(path,file_name2),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(lst)
            else:
                with open(os.path.join(path,file_name2),'a+') as fi:
                    csvwriter=csv.writer(fi)
                    csvwriter.writerow(new_field_names)
                    csvwriter.writerow(lst)

#new_file_sort()

del_create_analytics_folder()
course()
country()
email_domain_extract()
gender()
dob()
state()
blood_group()
new_file_sort()


