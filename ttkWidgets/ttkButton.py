#!/usr/bin/python

# Python 2.7.8
import Tkinter
import ttk

root = Tkinter.Tk()
# Buton flat
ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
btn = ttk.Button(text = "ttk.Button")
btn.pack()

style = ttk.Style()
style.map("C.TButton",
          foreground=[('pressed','red'), ('active', 'blue')],
          background=[('pressed','!disabled','black'), ('active', 'white')]
          )
colored_btn= ttk.Button(text="Test", style="C.TButton").pack()

style = ttk.Style()
style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()

root.title("ttk.Button exemplu")
root.geometry("200x200+100+100")
root.mainloop()
