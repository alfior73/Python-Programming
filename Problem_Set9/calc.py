from tkinter import *

def doOK():
    print("OK button clicked")

def doCancel():
    print("Cancel button clicked")

window = Tk()

btnOk = Button(window, text="OK", fg='blue', command=doOK)
btnCancel = Button(window, text="Cancel", bg='blue', command=doCancel)

btnOk.grid(row=1, column=1, padx=(2,10), pady=5)
btnCancel.place(x=72, y=5)

window.mainloop()