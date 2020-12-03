from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile() :
	global file 
	root.title("Untitled - Notepad")
	file = None
	TextArea.delete(1.0, END)


def openFile() :
	global file
	file = askopenfilename(defaultextension=".txt", filetypes = [("All Files", "*.*"), 
				("Text Documents", "*.txt")])
	if file == "" :
		file = None
	else :
		root.title(os.path.basename(file) + " - Notepad")
		TextArea.delete(1.0, END)
		f = open(file,"r")
		TextArea.insert(1.0, f.read())
		f.close()


def saveFile() :
	global file 
	if file == None :
		file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes = [("All Files", "*.*"), 
				("Text Documents", "*.txt")])
		if file == "" :
			file = None
		else :
			# Save as a new file
			f = open(file,'w')
			f.write(TextArea.get(1.0, END))
			f.close()
			root.title(os.path.basename(file) + " - Notepad")
	else :
		f = open(file,'w')
		f.write(TextArea.get(1.0, END))
		f.close()

def saveasFile() :
	pass

def quitFile() :
	root.destroy()

def cut() :
	TextArea.event_generate(("<<Cut>>"))

def copy() :
	TextArea.event_generate(("<<Copy>>"))

def paste() :
	TextArea.event_generate(("<<Paste>>"))

def find() :
	pass

def find_replace() :
	pass

def word_count() :
	pass

def char_count() :
	pass

def created_time() :
	pass

def modified_time() :
	pass

def about_notepad() :
	showinfo("Notepad", "Notepad by Sonaal and Dheeraj")



if __name__ == '__main__' :
	# Basic tkinter setup
	root = Tk()
	root.title("Untitled - Notepad")
	#root.wm_iconbitmap("Notepad icon")
	root.geometry("650x750")

	# Text Area
	TextArea = Text(root)
	TextArea.pack(expand = True, fill = BOTH)
	file = None

	# MenuBar
	MenuBar = Menu(root)

	# File Menu
	FileMenu = Menu(MenuBar, tearoff = 0)
	FileMenu.add_command(label = "New", command = newFile) # To create new file
	FileMenu.add_command(label = "Open", command = openFile) # To open already existing file
	FileMenu.add_command(label = "Save", command = saveFile) # To save the current file
	FileMenu.add_command(label = "Save As", command = saveasFile) # Save As
	FileMenu.add_separator() # -------------
	FileMenu.add_command(label = "Exit", command = quitFile)
	MenuBar.add_cascade(label = "File", menu = FileMenu)
	
	# Edit Menu
	EditMenu = Menu(MenuBar, tearoff = 0)
	EditMenu.add_command(label = "Cut", command = cut) # Cut option
	EditMenu.add_command(label = "Copy", command = copy) # Copy option
	EditMenu.add_command(label = "Paste", command = paste)# Paste option
	EditMenu.add_command(label = "Find", command = find) # Find option
	EditMenu.add_command(label = "Find & Replace", command = find_replace) # Find and replace option
	MenuBar.add_cascade(label = "Edit", menu = EditMenu)

	# Stats Menu
	StatsMenu = Menu(MenuBar, tearoff = 0)
	StatsMenu.add_command(label = "Word Count", command = word_count)
	StatsMenu.add_command(label = "Char Count", command = char_count)
	StatsMenu.add_command(label = "Created Time", command = created_time)
	StatsMenu.add_command(label = "Modified Time", command = modified_time)
	MenuBar.add_cascade(label = "Stats" , menu = StatsMenu)

	# Help Menu
	HelpMenu = Menu(MenuBar, tearoff = 0)
	HelpMenu.add_command(label = "About Notepad", command = about_notepad)
	MenuBar.add_command(label = "Help" , menu = HelpMenu)
	MenuBar.add_cascade(label="Help",menu=HelpMenu)
	root.config(menu = MenuBar)

	# Adding ScrollBar
	Scroll = Scrollbar(TextArea)
	Scroll.pack(side=RIGHT, fill= Y)
	Scroll.config(command =TextArea.yview)
	TextArea.config(yscrollcommand = Scroll.set)











	root.mainloop()
