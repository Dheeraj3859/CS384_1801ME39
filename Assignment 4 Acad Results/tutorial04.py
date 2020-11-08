import pandas as pd
import os
import csv
import shutil
path="./grades"

def create_delete_grade_folder():
	if os.path.exists(path)==False:
		os.mkdir(grades)
	else:
		shutil.rmtree(path)
		os.mkdir(path)

create_delete_grade_folder()

df = pd.read_csv('acad_res_stud_grades.csv')
print(df.head())
df.drop(['sl','timestamp','year'],axis=1,inplace=True)
print(df.head())
print(len(df))

for i in range(len(df)-30000):
	ro = df.loc[i]
	roll_no=ro['roll']
	file_name1 = roll_no+'_'+'individual'+'.csv'
	if os.path.exists(os.path.join(path,file_name1))==False:
		st1 = 'Roll: '+roll_no
		st2 = 'Semester Wise Details'
		sub = ro['sub_code']
		cre = ro['total_credits']
		typ = ro['sub_type']
		gra = ro['credit_obtained']
		sem = ro['sem']
		df2 = pd.DataFrame([[st1],[st2],['Subject','Credits','Type','Grade','Sem'],[sub,cre,typ,gra,sem]])
		file = './grades/'+file_name1
		df2.to_csv(file,mode='a+',index=False,header=False)
	else:
		sub = ro['sub_code']
		cre = ro['total_credits']
		typ = ro['sub_type']
		gra = ro['credit_obtained']
		sem = ro['sem']
		df2 = pd.DataFrame([[sub,cre,typ,gra,sem]])
		file = './grades/'+file_name1
		df2.to_csv(file,mode='a+',header=False,index=False)

def fun(s):
	if s=="AA":
		return 10
	elif s=='AB':
		return 9
	elif s=='BB':
		return 8
	elif s=='BC':
		return 7
	elif s=='CC':
		return 6
	elif s=='CD':
		return 5
	elif s=='DD':
		return 4
	elif s=='F':
		return 0
	elif s=='I':
		return 0

roll_no = df['roll'].unique()
print(len(roll_no))
for i in roll_no:
	print(i)
	file_name1=i+'_'+'overall'+'.csv'
	if os.path.exists(os.path.join(path,file_name1))==False:
		st = 'Roll: '+i
		st1 = 'Semester'
		st2 = 'Semester Credits'
		st3 = 'Semester Credits Cleared'
		st4 = 'SPI'
		st5 = 'Total Credits'
		st6 = 'Total Credits Cleared'
		st7 = 'CPI'
		df2 = pd.DataFrame([[st],[st1,st2,st3,st4,st5,st6,st7]])
		file = './grades/'+file_name1
		df2.to_csv(file,mode='a+',header=False,index=False)
		file_name = './grades/'+i+'_'+'individual'+'.csv'
		df_roll = pd.read_csv(file_name,skiprows=[0,1])
		cred_till_now=0
		cred_cleared=0
		cpi=0
		for i in range(1,9):
			sem=df_roll[df_roll['Sem']==i]
			sem = sem.reset_index()
			credi=0
			num=0
			for j in range(len(sem)):
				sub = sem.loc[j]
				num+=sub['Credits']*fun(sub['Grade'])
				credi+=sub['Credits']
			spi=round(num/credi,2)
			cpi = round((cred_till_now*cpi + credi*spi)/(cred_till_now+credi),2)
			cred_till_now+=credi
			df3 = pd.DataFrame([[i,credi,credi,spi,cred_till_now,cred_till_now,cpi]])
			tem_file = './grades/'+file_name1
			df3.to_csv(tem_file,mode='a+',header=False,index=False)





