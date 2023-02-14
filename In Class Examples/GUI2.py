from tkinter import *


def okButtonFunction():
        Outputlbl.config(text=inputtext.get())


window = Tk()

inputtext = StringVar()

OKbtn = Button(window, text="OK", font=("Helvetica", 22),
             command=okButtonFunction)

Outputlbl = Label(window, text="0", font=("Helvetica", 22))

textInputEnt = Entry(window, text="enter stuff here", textvariable=inputtext)


OKbtn.grid(row=2, column=1)
Outputlbl.grid(row=1, column=2)
textInputEnt.grid(row=1, column=0)

window.mainloop()
