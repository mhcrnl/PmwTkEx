#!/usr/bin/env python

title = "Text Editor"
geometry = "400x400+100+50"

#Aici s-a implementat functionarea in Python 2 si Python 3
try:
	# Python 2
	import Tkinter as tk
	import ScrolledText as tkst
	import tkMessageBox
	import Pmw
	import os
except ImportError:
	# Python 3
	import tkinter as tk
	import tkinter.scrolledtext as tkst
	import Pmw
	import os


class MyFrame(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
	
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self.textArea = tkst.ScrolledText(master=self.parent, undo=1)
		self.textArea.pack(fill="both", expand="yes", padx=6, pady=6)
		
		"""Adaugarea meniului din fereastra"""
		# Aici am creat un menubar care este configurat ca meniu in fereastra
		self.menubar = tk.Menu(parent)
		parent.config(menu= self.menubar)
		# am creat un meniu file care este un popup care contine comenzi
		self.fileMenu = tk.Menu(self.menubar)
		# adaugam o comanda in fileMenu
		self.fileMenu.add_command(label="New", command = None)
		self.fileMenu.add_command(label="Exit", command=parent.quit)
		
		# fileMenu este adaugat la menubar
		self.menubar.add_cascade(label="File", menu=self.fileMenu)
		"""Adaugarea editMenu -------------------------------------"""
		#Adaugarea unei noi file la menubar
		self.editMenu = tk.Menu(self.menubar)
		#Adaugam o commanda in editMenu
		self.editMenu.add_command(label="Undo")
		
		#Editmenu este adaugat la menubar
		self.menubar.add_cascade(label="Edit", menu=self.editMenu)
		"""---------------Adaugare searchMenu---------------------"""
		
		"""Adaugarea functionalitatilor aplicatiei in metode"""
		
		def fileNew(self):
			print "apelat"
		

		
       

def main():
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)
    MyFrame(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()
    
    #Adaugare Button pentru testare
    exitBtn = tk.Button(root, text="Exit", command=root.quit)
    exitBtn.pack()

if __name__ == "__main__":
	main()

   
    
