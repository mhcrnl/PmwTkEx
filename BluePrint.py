#!/usr/bin/python
#-*- coding:utf-8 -*-
"""Author: Mihai Cornel
Email: mhcrnl@gmail.com
Tel: 0722 27 07 96
Data: Sept/2015
File: celsius1.py
"""
title = 'Pmw.ButtonBox demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class BluePrint:
    def __init__(self, parent):
        self.entryCelsius = Pmw.EntryField(parent, labelpos='w',
                                           label_text='Celsius', validate=None)
        self.entryCelsius.pack()
        





########################Testare Aplicatiei ################################
def main():
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)
    root.geometry("400x350+300+250")
    #Butonul de inchidere al aplicatiei
    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    
    widget = BluePrint(root)
    root.mainloop()
    #root.destroy()

if __name__ == "__main__":
    main()

        
