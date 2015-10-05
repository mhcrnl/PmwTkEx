

from Tkinter import *
from tkMessageBox import askokcancel

class MyFrame(Frame):
    def __init__(self, parent=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.pack()
        widget = Button(self, text="Quit", command=self.quit)
        widget.pack(expand="YES", fill = "both", side="left")

    def quit(self):
        ans = askokcancel('Verify exit', "Realy quit?")
        if ans : Frame.destroy(self)

if __name__ == "__main__":
    root = MyFrame()
    root.mainloop()
    root.destroy()
