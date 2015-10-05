
from clasframe import MyFrame
import Tkinter

class MyFrame1(MyFrame):
    def __init__(self, parent=None, *args, **kwargs):
        MyFrame.__init__(self, parent, *args, **kwargs)
        self.pack()

        label = Tkinter.Label(text="nume")
        label.pack()

if __name__ == "__main__":
    root = MyFrame1()
    root.mainloop()
"""
    

root = Tkinter.Tk()
root.title("Fereastra din alta fila")
root.geometry("300x300+100+60")
exitbtn=Tkinter.Button(root, text="Quit", command=root.quit)
exitbtn.pack()
MyFrame(root)
root.mainloop()
root.destroy()
"""
