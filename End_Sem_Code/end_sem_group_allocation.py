import pandas as pd
import os
import shutil
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
    if os.path.exists(os.path.join(path,'groupsbranch_strength.csv'))==False:
        st1="BRANCH_CODE"
        st2="STRENGTH"
        df2=pd.DataFrame([[st1,st2]])
        file=path+'groupsbranch_strength.csv'
        df2.to_csv(file,mode='a+',index=False,header=False)
    for x in bran:
        df2=pd.DataFrame([[x[0],x[1]]])
        file=path+'groupsbranch_strength.csv'
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
        df1.to_csv(path1,mode='w',index=False,header=False)



def group_allocation(filename, number_of_groups):
    del_create_groups()
    branch_strength(filename)
    branch_details(filename)
    

	# Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
filename="Btech_2020_master_data.csv"
number_of_groups = int(input("Enter the number of groups"))
group_allocation(filename, number_of_groups)

