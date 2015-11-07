import Tkinter,sys, time
from Tkinter import *
from tkFileDialog import askopenfilename

	
def openfile():
	
	filename = askopenfilename(parent=window)
	f = open(filename)
	f.read()
	f.close()

def song():
	tkMessageBox.showinfo("Reset", "...Opened Successfully!")	
	A = Tkinter.Button(window, text ="Analyze Song", fg="green", command = analyzed)
	A.pack()
	
def msgbox():
	openfile()
	song()

def analyzed():
	tkMessageBox.showinfo("Analyze Song", "...Analyzed successfully!")
	tkMessageBox.showinfo("Genre determined", "Determined song genre according to analysis: ")
	tkMessageBox.showinfo("Correct", "Is this the correct genre?")
	Y = Tkinter.Button(window, text ="Yes")
	N = Tkinter.Button(window, text="No")
	Y.pack()
	N.pack()
	
import tkMessageBox
window = Tk()

B = Tkinter.Button(window, text ="Reset", fg="red")
B.pack()

S = Tkinter.Button(window, text ="Open Song", fg="blue", command = msgbox)
S.pack()



window.title("Genre-Sorter")
window.geometry("500x500")
window.mainloop()

        


