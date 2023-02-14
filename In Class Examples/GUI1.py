 Gui1

from tkinter import *

count = 0

def okButtonFunction():
    global count
    count = count + 1
    lbl.config(text=str(count))
    
def clearCount():
    global count
    count = 0
    lbl.config(text=str(count))

window = Tk()

btn = Button(window, text="OK", 
             cnf={"fg":"red", "bg":"green", "font": 18},
             command=okButtonFunction)

lbl = Label(window, text="0", font=("Helvetica", 22))

clearBtn = Button(window, text ="clear", font=("Helvetica", 18), command=clearCount)

btn.pack()
lbl.pack()
clearBtn.pack()

window.mainloop()

