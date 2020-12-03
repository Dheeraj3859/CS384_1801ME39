from tkinter import *
import random
questions = [
			
			"This is q1 ",
			"This is q2",
			"This is q3",
			"This is q4",
			"This is q5",
			"This is q6",
			"This is q7",
			"This is q8",
			"This is q9",
			"This is q10"
]

ans_choice = [

		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"],
		["1","2","3","4"]
]

indexes = []
def gen():
	global indexes
	while(len(indexes)<5):
		x=random.randint(0,9)
		if x in indexes:
			continue
		indexes.append(x)

user_ans=[]
ques = 1
def select():
	global radiovar,user_ans,lblquestion,r1,r2,r3,r4
	global ques
	x=radiovar.get()
	user_ans.append(x)
	if ques<5:
		lblquestion.config(text=questions[indexes[ques]])
	else:
		pass
	

def startquiz():
	global lblquestion,r1,r2,r3,r4
	lblquestion = Label(root,text=questions[indexes[0]],width=500,justify="center")
	lblquestion.pack()
	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)
	gen()
	r1 = Radiobutton(root,text=ans_choice[indexes[0]][0],variable=radiovar,value=0,command=select)
	r1.pack()
	r2 = Radiobutton(root,text=ans_choice[indexes[0]][1],variable=radiovar,value=1,command=select)
	r2.pack()
	r3 = Radiobutton(root,text=ans_choice[indexes[0]][2],variable=radiovar,value=2,command=select)
	r3.pack()
	r4 = Radiobutton(root,text=ans_choice[indexes[0]][3],variable=radiovar,value=3,command=select)
	r4.pack()


def start():
	labelimage.destroy()
	labeltext.destroy()
	btn.destroy()
	gen()
	startquiz()

root = Tk()
root.title("quiz app")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)
img1 = PhotoImage(file="hat.png")
labelimage = Label(root,image=img1,background="#ffffff")
labelimage.pack()

labeltext = Label(root,text="quiz",background="#ffffff")
labeltext.pack()
btn = Button(root,text="start",command=start)
btn.pack()
root.mainloop()