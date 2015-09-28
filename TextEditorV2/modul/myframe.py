import Tkinter

class MyFrame(Tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        Tkinter.Frame(self, parent, args, **kwargs)

def main():
    root = Tkinter.Tk()
    MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
