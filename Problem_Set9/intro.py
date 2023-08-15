from tkinter import *

window = Tk()

label = Label(window, text="Welcome to TKinter")
text = Text(window, cnf={'bg': 'yellow'})
button = Button(window, text="Click Me")

label.pack()
text.pack()
button.pack()

window.mainloop()