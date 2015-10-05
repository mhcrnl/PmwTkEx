#!/usr/bin/env python

from Tkinter import *
#import winsound
import os

class Alarm(Frame):
    def reapeater(self):
        print "\a"
        os.system("beep -f 555 -l 460")
        self.bell()
        self.after(self.msecs, self.reapeater)

    def __init__(self, parent, msecs):
        Frame.__init__(self)
        self.msecs = 1000
        self.pack()
        stoper = Button(self, text="Stop the beep!", command = self.quit)
        stoper.pack()
        stoper.config(bg='navy', fg='white', bd=8)
        self.stoper = stoper
        self.reapeater()


if __name__ == "__main__":
    root = Tk()
    Alarm(root, msecs=1000)
    root.mainloop()
    root.destroy()
