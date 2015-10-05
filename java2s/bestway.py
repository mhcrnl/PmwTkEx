import Tkinter as tk
from alarm import Alarm

class Demo1:
    def __init__(self, master):
        self.master= master
        self.frame= tk.Frame(self.master)
        self.button1=tk.Button(self.frame, text="new WIndow", width=25,
                               command=self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text="Quit", width=25,
                                    command=self.close_window)
        self.quitButton.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

class Demo3():
    def __init__(self, master):
        self.master=master
        self.frame = tk.Frame(self.master)
        self.demo2 = Demo1(self.frame)
        #self.alarm= Alarm(self.frame, msecs=1700)

        self.addBtn = tk.Button(self.master, text="BTN",
                                command=self.demo2.new_window)
        self.addBtn.pack()
        self.addBtn1 = tk.Button(self.master, text="BTN1",
                                command=self.runAlarm)
        self.addBtn1.pack()

        self.frame.pack()

    def runAlarm(self):
        self.alarm = Alarm(self.frame, msecs=1700)
        self.alarm.master.destroy()
    

def main():
    root=tk.Tk()
    app=Demo3(root)
    root.mainloop()

if __name__ == "__main__":
    main()
