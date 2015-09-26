#!/usr/bin/python
#-*- coding:utf-8 -*-
"""Author: Mihai Cornel
Email: mhcrnl@gmail.com
Tel: 0722 27 07 96
Data: Sept/2015
File: convertortemp.py
Program scris in: OS: Fedora 21 cu Python2.7.8 / Tkinter 8.6.2 / IDLE 2.7.8
Cerinte: Instalarea modului Pmw http://pmw.sourceforge.net/
"""
title = 'Pmw.ButtonBox demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class BluePrint:
    def __init__(self, parent):

        #--------------------------------------------------Begin/MainMenuBar
        #   Crearea unui Pmw.MegaToplevel
        #megaToplevel = Pmw.MegaToplevel(parent)
        #   Get the Tkinter.Toplevel from Pmw.MegaToplrvel
        #toplevel = megaToplevel.interior()
        #   Create the menu bar for the toplevel
        self.menuBar=Pmw.MainMenuBar(parent)
        #Configure the toplevel to use the menuBar
        parent.configure(menu = self.menuBar)
        self.menuBar.addmenu('File', 'Close this window')
        self.menuBar.addmenuitem('File', 'command', 'exit the app',
                                 label='Exit', command=parent.destroy)
        # Crearea meniului din bara File | Help
        self.menuBar.addmenu('Help', 'User manual', name='help')
        self.menuBar.addmenuitem('Help', 'command', 'About this App',
                                 command=self.execute,
                                 label = 'About..')
        #----------------------------------------------------End/MainMenuBar
        
        #---------------------------------------------------Begin/About
        Pmw.aboutversion('1.0')
        Pmw.aboutcopyright('Copyright Mihai Cornel 2015\n Free rights ')
        Pmw.aboutcontact(
            'For information about this application contact:\n' +
            '  My Help Desk\n' +
            '  Phone: 0722 27 07 96\n' +
            '  email: mhcrnl@gmail.com'
        )
        self.about = Pmw.AboutDialog(parent, applicationname = 'Convertor temperatura')
        self.about.withdraw()
        #---------------------------------------------------End/About

        # Begin/Celsius -------------------------------------------------------
        #Crearea unui Group
        self.celsius = Pmw.Group(parent, tag_text='Celsius to Fahrenheit')
        self.celsius.pack(fill='both', expand=0, padx=6, pady=6)
        #Adaugarea unui EntryField in Group
        self.entryCelsius = Pmw.EntryField(self.celsius.interior(), labelpos='w',
                                           label_text='Celsius:', validate=None)
        self.entryCelsius.focus()
        self.entryCelsius.pack(fill='both', padx=6, pady=6)
        #Adaugarea unui buton in aplicatie
        self.calculeazaBtn=Tkinter.Button(self.celsius.interior(),
                                          text='Calculeaza',
                                          command=self.celsiusToFahrenheit)
        self.calculeazaBtn.pack(side='right')
        #Adaugarea unei etichete pt afisarea rezultatului conversiei
        self.afisareLab=Tkinter.Label(self.celsius.interior(), text='Rezultat')
        self.afisareLab.pack(side='left')
        #End/Celsius--------------------------------------------------------

        #Begin/Fahrenheit---------------------------------------------------
        #Adaugarea unui Pmw.Group
        self.fahrenheit= Pmw.Group(parent, tag_text='Fahrenheit to Celsius')
        self.fahrenheit.pack(fill='both', expand=0, padx=6, pady=6)
        #Adaugarea unui Pmw.EntryField in Pmw.Group
        self.entryFahrenheit = Pmw.EntryField(self.fahrenheit.interior(), labelpos='w',
                                              label_text="Fahrenheit: ", validate=None)
        self.entryFahrenheit.pack(fill='both', padx=2, pady=6)
        #Adaugarea unui Tkinter.Button care sa calculeze
        self.calculeazaBtnF = Tkinter.Button(self.fahrenheit.interior(),
                                             text='Calculeaza',
                                             command=self.fahrenheitToCelsius)
        self.calculeazaBtnF.pack(side='right')
        #Adaugarea unei etichete Tkinter.Label pt afisarea rezultatului
        self.afisareLabF = Tkinter.Label(self.fahrenheit.interior(), text='Rezultat')
        self.afisareLabF.pack(side='left')
        #End/Fahrenheit------------------------------------------------------

        
    def celsiusToFahrenheit(self):
        print 'Functia celsiusToFahrenheit a fost apelata'
        self.rezultat = float(self.entryCelsius.get())*(9.0/5.0)+32
        self.afisareLab.config(text="Fahrenheit: " +str(self.rezultat))
        print self.rezultat

    def fahrenheitToCelsius(self):
        print 'Functia fahrenheitToCelsius() a fost apelata'
        self.rezultat = (float(self.entryFahrenheit.get())-32)*(5.0/9.0)
        self.afisareLabF.config(text='Celsius: ' + str(self.rezultat))
        print self.rezultat
        
    def execute(self):
        self.about.show()
        
########################Testare Aplicatiei ################################
def main():
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)
    root.geometry("400x350+300+250")
    #Butonul de inchidere al aplicatiei
    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    
    widget = BluePrint(root)
    root.mainloop()
    #root.destroy()

if __name__ == "__main__":
    main()

        
