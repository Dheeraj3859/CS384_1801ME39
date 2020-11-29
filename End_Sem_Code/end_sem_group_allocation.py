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

def extract_number(st):
    x=st.split('_')
    x1=x[1].split('.')
    re=x1[0][1:]
    return re

def branch_strength(filename):
    df = pd.read_csv(filename)
    bran = {}
    for i in df['Roll']:
        b=branch(i)
        if b in bran:
            bran[b]+=1
        else:
            bran[b]=1
    bran=sorted(bran.items(),key=lambda x: (-x[1],x[0]))
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

def get_unique_branches(filename):
    lst=[]
    df = pd.read_csv(filename)
    for i in df['Roll']:
        bran = branch(i)
        lst.append(bran)
    se = set(lst)
    unq=[]
    for x in se:
        unq.append(x)
    return unq

def sort_it(pa,number_of_groups):
    df = pd.read_csv(pa)
    if os.path.exists('./groups/stats_grouping.csv')==False:
        df60 = pd.read_csv('./groups/branch_strength.csv')
        lst=['group','total']
        for x in df60['BRANCH_CODE']:
            lst.append(x)
        df1=pd.DataFrame([lst])
        file='./groups/stats_grouping.csv'
        df1.to_csv(file,mode='a+',index=False,header=False)
    df60 = pd.read_csv('./groups/branch_strength.csv')
    lst_branch=[]
    for x in df60['BRANCH_CODE']:
        lst_branch.append(x)
    for i in range(1,number_of_groups+1):
        for j in range(len(df['group'])):
            x=df.loc[j]
            grp=x['group']
            if str(i) in grp and i==int(extract_number(grp)):
                lst1=[grp,x['total']]
                for b in lst_branch:
                    lst1.append(x[b])
                df_t=pd.DataFrame([lst1])
                file='./groups/stats_grouping.csv'
                df_t.to_csv(file,mode='a+',index=False,header=False)
    


def stats(filename,number_of_groups):
    files = os.listdir('./groups')
    for fi in files:
        if 'Group' in fi:
            if os.path.exists('./groups/stats grouping.csv')==False:
                lst=['group','total']
                #unq = get_unique_branches(filename)
                df60 = pd.read_csv('./groups/branch_strength.csv')
                #for b in unq:
                #    lst.append(b)
                for x in df60['BRANCH_CODE']:
                    lst.append(x)
                df1 = pd.DataFrame([lst])
                file_temp = './groups/stats grouping.csv'
                df1.to_csv(file_temp,mode='a+',index=False,header=False)

            dict1={}
            fil = './groups/'+fi
            df2 = pd.read_csv(fil)
            total = len(df2['Roll'])
            for ro in df2['Roll']:
                br = branch(ro)
                if br in dict1:
                    dict1[br]+=1
                else:
                    dict1[br]=1
            #unq = get_unique_branches(filename)
            lst_temp=[fi,total]
            #for x in unq:
            #    lst_temp.append(dict1[x])
            df60 = pd.read_csv('./groups/branch_strength.csv')
            for x in df60['BRANCH_CODE']:
                lst_temp.append(dict1[x])
            df8 = pd.DataFrame([lst_temp])
            file_temp1='./groups/'+'stats grouping.csv'
            df8.to_csv(file_temp1,mode='a+',index=False,header=False)

    df9 = pd.read_csv('./groups/stats grouping.csv')
    df9.sort_index(ascending=True,inplace=True)
    lst=['group','total']
    df60 = pd.read_csv('./groups/branch_strength.csv')
    for x in df60['BRANCH_CODE']:
        lst.append(x)
    df_te1 = pd.DataFrame([lst])
    f1 = './groups/stats grouping.csv'
    df_te1.to_csv(f1,mode='w',index=False,header=False)
    df9.to_csv(f1,mode='a+',index=False,header=False)
    sort_it('./groups/stats grouping.csv',number_of_groups)

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

    stats(filename,number_of_groups)
    os.remove('./groups/stats grouping.csv')

filename="Btech_2020_master_data.csv"
number_of_groups = int(input("Enter the number of groups\n"))
group_allocation(filename, number_of_groups)

