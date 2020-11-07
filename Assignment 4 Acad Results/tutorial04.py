import pandas as pd
import os
import csv
path="./grades"
df = pd.read_csv('acad_res_stud_grades.csv')
print(df.head())
for col in df:
	print(col)
roll_list = df['roll'].unique()
for roll_no in roll_list:
	string1 = roll_no+'_'+'individual'+'.csv'
	string2 = roll_no+'_'+'overall'+'.csv'
	with open(os.path.join(path,string1),'a+') as fi:
		pass
	with open(os.path.join(path,string2),'a+') as fi:
		pass


