import Tkinter as tk
import csv

class SaveFileCsv(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.entName = tk.Entry()
        self.entName.pack()

        self.entTel = tk.Entry()
        self.entTel.pack()

        self.btnSave = tk.Button(text="Save CSV", command=self.saveCSV)
        self.btnSave.pack()

        self.btnClose = tk.Button(text="Close", command=self.quit)
        self.btnClose.pack()
        
    def saveCSV(self):
        with open('formular2.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(self.entName.get()+ self.entTel.get())
        

if __name__ == '__main__':
    app = SaveFileCsv()
    app.mainloop()
    app.destroy()
