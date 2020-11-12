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

"""    

def rename_Sherlock(folder_name):
    # rename Logic 
    

def rename_Suits(folder_name):
    # rename Logic 
    
"""
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


title = input()
if title=='Game of Thrones':
	rename_Game_of_Thrones(title)
if title=='How I Met Your Mother':
	rename_How_I_Met_Your_Mother(title)
