#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Utilizarea importului multiplu pt functionarea codului in Python 2 si Python3
try:
    #Python 2
    import Tkinter as tk
except ImportError:
    #Python 3
    import tkinter as tk

title = "Toolbar Buttons"
geometry = "400x400+100+100"

class ToolbarButtons():
    def __init__(self, master):
        self.master = master
        #Begin/adaugare toolbar in fereastra-----------------------
        toolbar=tk.Frame(master)
        #-------------------------BEGIN/Adaugare buton New
        fotoNew =tk.PhotoImage(file="reflectionsm.GIF")
        newBtn = tk.Button(toolbar, text="New", image=fotoNew, compound="left")
        newBtn.pack(side="left", padx=2, pady=2)
        newBtn.image=fotoNew                       
                               
        #-------------------------END/Adaugare buton New
        openBtn=tk.Button(toolbar, text="Open", width=6)
        openBtn.pack(side="right", padx=2, pady=2)
        #-------------------------END/Add Button Open
        fotoClose=tk.PhotoImage(file='close.gif')
        closeBtn=tk.Button(toolbar, text="Close", image=fotoClose,
                           compound="left", height=20, command=master.quit)
        closeBtn.pack(side="right", padx=2, pady=2)
        closeBtn.image=fotoClose

        toolbar.pack(side="top", fill="x")
        #END/Adaugare toolbar in fereastra ------------------------


if __name__ == "__main__":
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)
    ToolbarButtons(root)
    root.mainloop()
    root.destroy()
