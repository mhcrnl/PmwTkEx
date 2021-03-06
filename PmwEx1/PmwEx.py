title = 'Pmw.EXAMPLE demonstration'
import sys

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):

        self.widget1 = Pmw.Counter(parent)
        self.widget1.setentry('1')
        self.widget1.pack()

        self.widget2 = Pmw.Counter(parent, increment=10)
        self.widget2.setentry('100')
        self.widget2.pack()

###############################################################

# Create demo in root window for testing
if __name__=='__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)

    exitButton = Tkinter.Button(root, text='Exit', command=root.quit)
    exitButton.pack(side='bottom')
    widget=Demo(root)
    root.mainloop()
