import os
import re
"""
path = './Subtitles/Sherlock'
files = os.listdir(path)
season_padding = int(input())
episode_padding = int(input())
for f in files:
	print(f)

	x=f.split('.')
	s=x[1]
	s_s=""
	s_e=""
	if 'E' in s:
		s1=s.split('E')
		s_s=s1[0]
		s_e+='E'+s1[1]
	else:
		s_s=s
		s_e=x[2]
	#print(s_s,s_e)
	v1=s_s[1:]
	#print(v1,s_e[1:])
	#print("v1=",v1,"v1+5=",v1+5)
"""
def rename_Sherlock(folder_name):
	#rename Logic
	
	path = './Subtitles/Sherlock'
	files=os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
		print(f)

rename_Sherlock(Sherlock)