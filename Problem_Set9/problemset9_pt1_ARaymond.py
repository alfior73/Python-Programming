from tkinter import *


class HelloWorld:

    def __init__(self):
        window = Tk()
        window.title("Hello World")

        self.text1 = StringVar()
        

        Label(window, text="Message", font="Helvetica 14").grid(
            row=1, column=1, sticky=W)
        Entry(window, textvariable=self.text1, justify=RIGHT).grid(
            row=1, column=2, padx=(0, 5))

        

        Label(window, text=None).grid(row=3, column=1, sticky=W)

        
        Button(window, text="Click Me", command=self.print,
               font="Helvetica 14").grid(row=10, column=2, padx=(100, 5), pady=5)

        window.mainloop()

    def print(self):
        

        self.text1.set("Hello")
        


HelloWorld()
