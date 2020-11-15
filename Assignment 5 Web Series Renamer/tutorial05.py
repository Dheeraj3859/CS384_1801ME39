import os
import re
def rename_Game_of_Thrones(folder_name):
	# rename Logic
	path = './Subtitles/Game of Thrones'
	files = os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
		#print('f=',f)
		stri=""
		x=f.split(' - ')
		for c in f:
			if c=='.':
				break
			else:
				stri+=c
		res=""
		res+=x[0]+' - '
		temp=x[1].split('x')
		season="Season "
		episode="Episode "
		for i in range(0,season_padding-len(temp[0])):
			season+='0'
		for i in range(0,episode_padding-len(temp[1])):
			episode+='0'
		season+=temp[0]
		episode+=temp[1]
		res+=season+" "
		res+=episode
		res+=' - '
		s = x[2]
		s1=x[2].split('.')
		res+=s1[0]
		if s[len(s)-1]=='t':
			res+='.srt'
		else:
			res+='.mp4'
		source_file=os.path.join(path,f)
		dest_file=os.path.join(path,res)
		os.rename(source_file,dest_file)
		#print(res) 

def rename_Suits(folder_name):
	# rename Logic
	path = './Subtitles/Suits'
	files = os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
		stri=""
		x=f.split(' - ')
		for c in f:
			if c=='.':
				break
			else:
				stri+=c
		res=""
		res+=x[0]+' - '
		temp=x[1].split('x')
		season="Season "
		episode="Episode "
		for i in range(0,season_padding-len(temp[0])):
			season+='0'
		for i in range(0,episode_padding-len(temp[1])):
			episode+='0'
		season+=temp[0]
		episode+=temp[1]
		res+=season+" "
		res+=episode
		res+=' - '
		s = x[2]
		s1=x[2].split('.')
		res+=s1[0]
		if s[len(s)-1]=='t':
			res+='.srt'
		else:
			res+='.mp4'
		#print(res)
		source_file=os.path.join(path,f)
		dest_file=os.path.join(path,res)
		os.rename(source_file,dest_file)

def rename_How_I_Met_Your_Mother(folder_name):
	# rename Logic
	path = './Subtitles/How I Met Your Mother'
	files = os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
		stri=""
		x=f.split(' - ')
		for c in f:
			if c=='.':
				break
			else:
				stri+=c
		res=""
		res+=x[0]+' - '
		temp=x[1].split('x')
		season="Season "
		episode="Episode "
		for i in range(0,season_padding-len(temp[0])):
			season+='0'
		for i in range(0,episode_padding-len(temp[1])):
			episode+='0'
		season+=temp[0]
		episode+=temp[1]
		res+=season+" "
		res+=episode
		res+=' - '
		s = x[2]
		s1=x[2].split('.')
		res+=s1[0]
		if s[len(s)-1]=='t':
			res+='.srt'
		else:
			res+='.mp4'
		#print(res)
		source_file=os.path.join(path,f)
		dest_file=os.path.join(path,res)
		os.rename(source_file,dest_file)

def rename_Sherlock(folder_name):
	#rename Logic
	
	path = './Subtitles/Sherlock'
	files=os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
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

		res=""
		res+=x[0]+' - '
		v1=s_s[1:]
		v1_temp=""
		for i in range(0,season_padding-len(v1)):
			v1_temp+='0'
		v1_temp+=v1
		res+='Season '+v1_temp+' '
		v2=s_e[1:]
		v2_temp=""
		for i in range(0,episode_padding-len(v2)):
			v2_temp+='0'
		v2_temp+=v2
		res+='Episode '+v2_temp
		res+='.'
		res+=x[len(x)-1]
		#print(res)
		source_file=os.path.join(path,f)
		dest_file=os.path.join(path,res)
		os.rename(source_file,dest_file)

def rename_FIR(folder_name):
	path = './Subtitles/FIR'
	files = os.listdir(path)
	season_padding=int(input())
	episode_padding=int(input())
	for f in files:
		x=f.split('-')
		res=""
		x=[k.strip() for k in x]
		#print(x[len(x)-1])
		res+=x[0]+' '
		ep=""
		for l in x:
			if 'Episode' in l and 'Full' not in l:
				ep=l
				break
			elif 'Ep' in l:
				ep=l
				break
		ep_lst = ep.split(' ')
		#print(ep_lst)
		
		epnum = ep_lst[1] 
		res_ep=""
		for i in range(episode_padding-len(epnum)):
			res_ep+='0'
		res_ep+=epnum
		res+='Episode '+res_ep
		if 'srt' in x[len(x)-1]:
			res+='.srt'
		else:
			res+='.mp4'
		#print(res)
		source_file=os.path.join(path,f)
		dest_file=os.path.join(path,res)
		os.rename(source_file,dest_file)
		

    # rename Logic
title = input()
if title=='Game of Thrones':
	rename_Game_of_Thrones(title)
if title=='How I Met Your Mother':
	rename_How_I_Met_Your_Mother(title)
if title=='Suits':
	rename_Suits(title)
if title=='Sherlock':
	rename_Sherlock(title)
if title=='FIR':
	rename_FIR(title)
