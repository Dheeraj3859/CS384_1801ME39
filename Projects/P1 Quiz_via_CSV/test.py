import multiprocessing
import pandas as pd
from tkinter import *
import sqlite3
import time
import hashlib
conn = sqlite3.connect('project1_quiz_cs384.db')
c = conn.cursor()
def show_data():
	conn = sqlite3.connect('project1_quiz_cs384.db')
	c = conn.cursor()
	c.execute("SELECT * FROM project1_registration")
	lst = c.fetchall()
	for item in lst:
		print(item)
#c.execute("SELECT * FROM project1_registration WHERE roll=(?) AND password=(?)",(username,hash_pass))

show_data()
"""
root=Tk()
root.geometry("400x300")
tim=int(input("input the time in mins\n"))
tim*=60
Label(root,text='time').place(x=0,y=0)
l1 = Label(root,text=str(tim))
l1.place(x=10,y=0)
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
	print("Your time is up")
	root.destroy()

def fun():
	k=1
	while True:
		k+=1
		time.sleep(1)
		if k==15:
			print(f'the value of k is {k}')
			break
		else:
			print(f'the value of k is {k}')
p1 = multiprocessing.Process(target=countdown)
p2 = multiprocessing.Process(target=fun)
p1.start()
p2.start()
p1.join()
p2.join()

#print("hello")
root.mainloop()
"""






