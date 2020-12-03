from tkinter import *

# to create a window
root = Tk()
# root window is the parent window
fram = Frame(root)

# Creating Label, Entry Box, Button
# and packing them adding label to
# search box
Label(fram, text='Find').pack(side=LEFT)

# adding of single line text box

edit = Entry(fram)
# positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)
# setting focus
#edit.focus_set()

# adding of search button
Find = Button(fram, text='Find')
Find.pack(side=LEFT)

Label(fram, text="Replace With ").pack(side=LEFT)

edit2 = Entry(fram)
edit2.pack(side=LEFT, fill=BOTH, expand=1)
#edit2.focus_set()

replace = Button(fram,text="FindNReplace")
replace.pack(side=LEFT)

#now creating refresh button
refresh = Button(fram,text='Refresh')
refresh.pack(side=LEFT)
fram.pack(side=TOP)

#creating a text box in root
text = Text(root)
text.insert('1.0',""" Type your text""")
text.pack(side=BOTTOM)

def find(*args):
	text.tag_remove('found','1.0',END)
	s = edit.get()
	if (s):
		idx = '1.0'
		while 1:
			idx = text.search(s,idx,nocase=1,stopindex=END)
			if not idx:
				break
			lastidx = 
			pass










root.mainloop()