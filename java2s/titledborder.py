from Tkinter import *
from alarm import Alarm

class TitledBorder(Frame):
    def __init__(self, parent=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        f = Frame(parent, width=400, height=200)
        self.xf = Frame(f, relief=GROOVE, borderwidth=2)
        Label(self.xf, text="Python").pack(pady =10)
        Button(self.xf, text="Quit", state=DISABLED).pack(side=LEFT,
                                                          padx=5, pady=8)
        Button(self.xf, text="Close", command=self.quit).pack(side=RIGHT, padx=5,
                                                              pady=8)

        self.xf.place(relx=0.01, rely =0.125, anchor=NW)
        Label(f, text="TitledBorder").place(relx=.06, rely=0.125, anchor=W)
        f.pack()

        f1 = Frame(parent, width=500, height =100)
        self.xf2 = Frame(f1, relief=GROOVE, borderwidth=2)
        self.msecs=12
        Label(self.xf2, text="Eticheta", msecs).pack()
        
        self.xf2.place(relx=0.01, rely=0.156, anchor=SW)
        f1.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Titled Border")
    root.geometry("400x400+100+100")
    TitledBorder(root)
    root.mainloop()
    root.destroy()
        
    
    
