import os
import sqlite3
import hashlib
import pandas as pd
import multiprocessing
import threading 
import time 
from tkinter import *
#if os.path.exists('project1_quiz_cs384.db')==True:
#	os.remove('project1_quiz_cs384.db')
def hash_password(password):
	encoded_password = hashlib.sha256(password.encode())
	hashed_password = encoded_password.hexdigest()
	return hashed_password

def countdown():
	global tim,l1,root
	while tim>0:
		time.sleep(1)
		l1.destroy()
		mins,secs=(tim//60,tim%60)
		st = str(mins)+':'+str(secs)
		l1 = Label(root,text=st)
		l1.place(x=40,y=0)
		root.update()
		tim-=1
	#print("Your time is up")
	root.destroy()


def register():
	name = input("Enter your name\n")
	roll = input("Enter your roll number\n")
	password = input("Enter your password\n")
	hashed_password = hash_password(password)
	whatsapp_number = input("Enter your whatsapp number\n")
	#print(name,roll,hashed_password,whatsapp_number)
	c.execute("INSERT INTO project1_registration VALUES (?,?,?,?)",(name,roll,hashed_password,whatsapp_number))
	conn.commit()
	print("Successfully registed!!")


def show_data():
	conn = sqlite3.connect('project1_quiz_cs384.db')
	c = conn.cursor()
	c.execute("SELECT * FROM project1_registration")
	lst = c.fetchall()
	for item in lst:
		print(item)

def get_time(df):
	lst=[]
	for x in df:
		lst.append(x)
	time=lst[len(lst)-1].split('=')
	s = ""
	for k in time[1]:
		if k.isdigit()==True:
			s+=k
		else:
			break
	ti = int(s)
	return ti
def fun_time():
	global tim,resp_flag
	while tim>0:
		time.sleep(1)
		if resp_flag==1:
			break

def fun_input():
	global user_response
	global resp_flag,q_index,next_flag
	print("Enter -1 if you don't want to attempt")
	user_response = input("Enter your option\n")
	if len(user_response)!=0 and user_response!='-1':
		resp_flag=1
	next_flag=input(("enter the question number which you want to go or press n to to to next question\n"))
	if next_flag.isdigit():
		q_index=int(next_flag)-1
	else:
		q_index+=1

def quiz_questions():
	global q_index,df,root,over,next_flag
	global tim,p1,p2
	le = len(df['ques_no'])
	attempted=0
	while tim>0 and q_index<le:
		row=df.loc[q_index]
		print('Question ',row['ques_no'],')',end=' ')
		print(row['question'],end='\n')
		print('Option 1) ',row['option1'],end='\n')
		print('Option 2) ',row['option2'],end='\n')
		print('Option 3) ',row['option3'],end='\n')
		print('Option 4) ',row['option4'],end='\n')
		global resp_flag,user_response
		resp_flag=0
		fun_input()
		if resp_flag==1:
			attempted+=1
	
	print("quiz over",end='\n')
	p1.terminate()
	print("Total quiz questions :", le)
	print("Total attempted questions :", attempted)

def test_interface():

	def get_quiz():
		global quiz_num
		global student_name
		global username
		print(f"the entered quiz is {quiz_num}",end='\n')
		quiz_file = './quiz_wise_questions/'+quiz_num+'.csv'
		global df
		df = pd.read_csv(quiz_file)
		global tim
		tim = get_time(df)*60
		print(f'the quiz time is {tim//60} min',end='\n')
		global root,l1 
		root=Tk()
		root.title("Test details and user details")
		root.geometry("400x300")
		Label(root,text='time').place(x=0,y=0)
		l1 = Label(root,text=str(tim))
		l1.place(x=130,y=0)
		l2 = Label(root,text=student_name)
		l2.place(x=0,y=25)
		l3 = Label(root,text=username)
		l3.place(x=0,y=50)
		global q_index
		q_index=0
		global p1,p2
		p1 = multiprocessing.Process(target=countdown)
		p2 = threading.Thread(target=quiz_questions)
		p1.start()
		p2.start()
		p1.join()
		p2.join()
		root.mainloop()
		#print(df.head())
	global quiz_num
	quiz_num=input("Enter the quiz number that you want to attempt\n")
	
	get_quiz()
	#root.mainloop()
	
	

#connecting to our project database
conn = sqlite3.connect('project1_quiz_cs384.db')
c = conn.cursor()

#now creating table inside our database
#creating project1_registration table 
if os.path.exists('project1_quiz_cs384.db')==False:

	c.execute("""CREATE TABLE project1_registration(

					name text,
					password text,
					roll text,
					whatsapp_number INTEGER
		)""")

	#creating project1_marks table
	c.execute("""CREATE TABLE project1_marks(

					roll text,
					quiz_num REAL,
					total_marks REAL
		)""")

# now creating the login portal
user_choice=input(("Do you want to register or login\n"))
user_choice=user_choice.lower()

def login():
	print("---------------------------Login Page------------------------\n")
	global username
	global student_name
	username = input("Enter your username\n")
	password = input("Enter the password\n")
	hash_pass = hash_password(password)
	c.execute("SELECT * FROM project1_registration")
	lst = c.fetchall()
	flag=0
	print(lst)
	for data in lst:
		if username in data and hash_pass in data:
			student_name=data[0]
			flag=1
			break
	if flag==0:
		print("You have not registered yet!!...redirecting you to registration page\n")
		register()
	else:
		print("You have logged in!!\n")
		test_interface()


if user_choice=='login':
	login()

else:
	#now register
	print("---------------------------Registration Page------------------------\n")
	register()
	print("you have registered now login\n")
	login()
	
	
show_data()

#os.remove('project1_quiz_cs384.db')