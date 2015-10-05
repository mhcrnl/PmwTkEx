#!/usr/bin/env python

from Tkinter import *
from alarm import Alarm

class AlarmHide(Alarm):
    def reapeater(self):
        self.bell()
        if self.shown:
            self.stoper.pack_forget()
        else:
            self.stoper.pack()
        self.shown = not self.shown
        self.after(self.msecs, self.reapeater)
    def __init__(self, msecs = 1000):
        self.shown =0
        Alarm.__init__(self,parent, msecs)

if __name__ == "__main__":
    root = Tk()
    AlarmHide(root, msecs=500)
    root.mainloop()
