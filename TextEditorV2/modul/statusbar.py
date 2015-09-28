#!/usr/bin/python

import Tkinter as tk
import ttk
import user


class StatusBar(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.label = ttk.Label(self, relief='sunken', anchor='w')
        self.label.pack(fill='x')

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

def main():
    root = tk.Tk()
    StatusBar(root)
    root.mainloop()

if __name__ == '__main__':
    main()
