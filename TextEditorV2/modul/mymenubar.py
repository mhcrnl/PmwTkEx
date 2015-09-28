#!/usr/bin/python

import Tkinter as tk
import Tkinter
import ttk
import user

class MyMenubar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        filemenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=filemenu)
        filemenu.add_command(label="New", command=self.callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, command=self.quit)

        helpmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)

    def callback(self):
        print "Metoda callback() a fost apelata"

       
def main():
    root = tk.Tk()
    root.config(menu=MyMenubar(root))
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
