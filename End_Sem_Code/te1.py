import pandas as pd
import os
path='./groups'
files = os.listdir(path)
for x in files:
	st1=x.split('.')
	if len(st1[0])!=2:
		continue
	path1=os.path.join(path,x)
	df1=pd.read_csv(path1)
	df1.sort_index(ascending=False,inplace=True)
	df1.to_csv(path1,mode='w',index=False,header=False)
	print(df1.head())

	