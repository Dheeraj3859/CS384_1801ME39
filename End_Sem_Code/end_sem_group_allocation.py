import pandas as pd
import os
import shutil
from queue import Queue
path='./groups/'

def del_create_groups():
    if os.path.exists("./groups")==False:
        os.mkdir("./groups")
    else:
        shutil.rmtree('./groups')
        os.mkdir('./groups')

def branch(roll):
    res=""
    for x in roll:
        if x.isdigit()==False:
            res+=x
    return res


def branch_strength(filename):
    df = pd.read_csv(filename)
    bran = {}
    for i in df['Roll']:
        b=branch(i)
        if b in bran:
            bran[b]+=1
        else:
            bran[b]=1
    bran=sorted(bran.items(),key=lambda x: (x[1],x[0]),reverse=False)
    if os.path.exists(os.path.join(path,'branch_strength.csv'))==False:
        st1="BRANCH_CODE"
        st2="STRENGTH"
        df2=pd.DataFrame([[st1,st2]])
        file=path+'branch_strength.csv'
        df2.to_csv(file,mode='a+',index=False,header=False)
    for x in bran:
        df2=pd.DataFrame([[x[0],x[1]]])
        file=path+'branch_strength.csv'
        df2.to_csv(file,mode='a+',index=False,header=False)
    

def branch_details(filename):
    df = pd.read_csv(filename)
    for i in range(len(df['Roll'])):
        ro=df.loc[i]
        bran=branch(ro['Roll']).upper()
        file=path+bran+'.csv'
        if os.path.exists(file)==False:
            df1=pd.DataFrame([['Roll','Name','Email']])
            df1.to_csv(file,mode='a+',index=False,header=False)
        df2=pd.DataFrame([[ro['Roll'],ro['Name'],ro['Email']]])
        df2.to_csv(file,mode='a+',index=False,header=False)    
    
    #now to sort the csv files based on roll number
    files=os.listdir(path)
    for x in files:
        st1=x.split('.')
        if len(st1[0])!=2:
            continue
        path1=os.path.join(path,x)
        df1=pd.read_csv(path1)
        df1.sort_index(ascending=True,inplace=True)
        df_temp=pd.DataFrame([['Roll','Name','Email']])
        df_temp.to_csv(path1,mode='w',index=False,header=False)
        df1.to_csv(path1,mode='a+',index=False,header=False)


def get_padded_string(num):
    st=str(num)
    if len(st)==2:
        return st
    else:
        return '0'+st

def group_allocation(filename, number_of_groups):
    del_create_groups()
    branch_strength(filename)
    branch_details(filename)
    
    df = pd.read_csv('./groups/branch_strength.csv')
    groups=number_of_groups
    q=Queue()

    for group in range(1,groups+1):
        group_file='Group_G'+get_padded_string(group)+'.csv'
        for ind in range(len(df['BRANCH_CODE'])):
            x=df.loc[ind]
            strength=x[1]
            stud=strength//groups
            file='./groups/'+x[0]+'.csv'
            df1 = pd.read_csv(file)
            for index in range(stud*(group-1),stud*group):
                student = df1.loc[index]
                file_path='./groups/'+group_file
                if os.path.exists(file_path)==False:
                    df4 = pd.DataFrame([['Roll','Name','Email']])
                    df4.to_csv(file_path,mode='a+',index=False,header=False)
                df5 = pd.DataFrame([[student['Roll'],student['Name'],student['Email']]])
                df5.to_csv(file_path,mode='a+',index=False,header=False)

    for i in range(len(df['BRANCH_CODE'])):
        x=df.loc[i]
        f = './groups/'+x[0]+'.csv'
        df6 = pd.read_csv(f)
        stud=x[1]//groups
        for j in range(stud*groups,x[1]):
            v = df6.loc[j]
            q.put((v['Roll'],v['Name'],v['Email']))

    index1 = 1
    while q.empty()==False:
        if index1>groups:
            index1=1
        group_file1='Group_G'+get_padded_string(index1)+'.csv'
        path_te = './groups/'+group_file1
        xt=q.get()
        df7 = pd.DataFrame([[xt[0],xt[1],xt[2]]])
        df7.to_csv(path_te,mode='a+',index=False,header=False)
        index1+=1

	# Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
filename="Btech_2020_master_data.csv"
number_of_groups = int(input("Enter the number of groups"))
group_allocation(filename, number_of_groups)

