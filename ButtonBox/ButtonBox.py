#!/usr/bin/python

title = "ButtonBox demonstratie"

# Import Pmw from this directory tree, if needed
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class ButtonBox:
    def __init__(self, parent):
        #Crearea si afisarea butoanelor
        self.buttonBox = Pmw.ButtonBox(parent,
                                       labelpos = 'nw',
                                       label_text = 'ButtonBox: ',
                                       frame_borderwidth = 2,
                                       frame_relief = 'groove')
        self.buttonBox.pack(fill = 'both',
                            expand =1,
                            padx=10,
                            pady = 10)
        # Adaugarea catorva butoane in Button box
        self.buttonBox.add('OK', command=self.ok)
        self.buttonBox.add('Apply', command=self.apply)
        self.buttonBox.add('Cancel', command=self.cancel)
        
        #Adaugarea EntryField
        self.entryCelsius = Pmw.EntryField(parent, labelpos='w',
										label_text='Celsius: ',
										validate=None)
										
			
	self.entryCelsius.pack(fill='both',
	expan=1, padx=10, pady=10)
	
										
        

        #Setarea butonului default <Return> is hit
        self.buttonBox.setdefault('OK')
        # parent.bind('<Return>', self._processReturnKey)
        parent.focus_set()

        #Make all the buttons the same width
        self.buttonBox.alignbuttons()
	'''
    def _procesReturnKey(self, event):
        self.buttonBox.invoke()
	'''
    def ok(self):
        print 'ati apasat butonul ok'

    def apply(self):
        print 'ati apasat butonul apply'

    def  cancel(self):
        print 'ati apasat butonul cancel'

#####################################################################

#Crearea ButtonBox Din root window pentru testare
if __name__=='__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)

    exitButton=Tkinter.Button(root, text='Exit', command=root.destroy)
    exitButton.pack(side='bottom')
    widget=ButtonBox(root)
    root.mainloop()
