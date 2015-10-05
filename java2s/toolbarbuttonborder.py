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
        
        # Adaugare TitledBorder--------------------
        borderToolbar = tk.Frame(master, width=400, height=80, padx=12,
                                 pady=12, bg='red')
        #Begin/adaugare toolbar in fereastra-----------------------
        toolbar=tk.Frame(borderToolbar, relief="groove", borderwidth=6,
                         bg='blue', width=150, height=100)
        #-------------------------BEGIN/Adaugare buton New
        #Add photo 01.gif
        photo1=tk.PhotoImage(file="reflectionsm.GIF")
        newBtn = tk.Button(toolbar, image=photo1, text="NEW",
                           compound="left")
        newBtn.pack(side="left", padx=2, pady=2)
        newBtn.image=photo1
        #-------------------------END/Adaugare buton New
        openBtn=tk.Button(toolbar, text="Open", width=6)
        openBtn.pack(side="right", padx=2, pady=2)
        #-------------------------END/Add Button Open
        closeBtn=tk.Button(toolbar, text="Close", width=6, command=master.quit)
        closeBtn.pack(side="right", padx=2, pady=2)

        toolbar.place(relx=0.01, rely=0.125, anchor="nw")#pack(side="top", fill="x")
        #END/Adaugare toolbar in fereastra ------------------------
        tk.Label(borderToolbar, text="Toolbar widget").place(relx=.06, rely=0.125,
                                                      anchor="w")
        borderToolbar.pack()
        
        foto=tk.PhotoImage(file="01.gif")
        gifBtn = tk.Button(master, image=foto)
        gifBtn.pack()
        gifBtn.image=foto

if __name__ == "__main__":
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)
    ToolbarButtons(root)
    root.mainloop()
    root.destroy()
