#!/usr/bin/python

import Tkinter as tk
import ttk
import user
import mymenubar
import statusbar


class MyRoot(tk.Tk):
    """Clasa container pentru toate celelalte clase"""
    def __init__(self, *args, **kwargs):
        """Initializarea superclasei"""
        tk.Tk.__init__(self, *args, **kwargs)

        self.menu = MyMenubar(self)
        self.config(menu = self.menu)

        self.status = self.StatusBar()
        self.status.pack(side="bottom", fill='x')

def main():
    root = MyRoot()
    root.title("Irina's TextEditor")
    
    root.geometry("400x400+150+150")
    #root.config(menu = MyMenubar(self))
    root.mainloop()

if __name__ == '__main__':
    main()
