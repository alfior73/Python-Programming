from tkinter import *


class Calculations:

    def __init__(self):
        window = Tk()
        window.title("Calculations")

        self.number1 = StringVar()
        self.number2 = StringVar()
        self.total_add = StringVar()
        self.total_subtract = StringVar()
        self.total_multiply = StringVar()
        self.total_divide = StringVar()

        Label(window, text="Number 1", font="Helvetica 14").grid(
            row=1, column=1, sticky=W)
        Entry(window, textvariable=self.number1, justify=RIGHT).grid(
            row=1, column=2, padx=(0, 5))

        Label(window, text="Number 2", font="Helvetica 14").grid(
            row=2, column=1, sticky=W)
        Entry(window, textvariable=self.number2, justify=RIGHT).grid(
            row=2, column=2, padx=(0, 5))

        Label(window, text=None).grid(row=3, column=1, sticky=W)

        Label(window, text="Total Added:", font="Helvetica 16").grid(
            row=4, column=1, sticky=W)
        Label(window, textvariable=self.total_add, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=4, column=2, sticky=E)

        Label(window, text="Total Subtract:", font="Helvetica 16").grid(
            row=5, column=1, sticky=W)
        Label(window, textvariable=self.total_subtract, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2, sticky=E)

        Label(window, text="Total Multiplied:", font="Helvetica 16").grid(
            row=6, column=1, sticky=W)
        Label(window, textvariable=self.total_multiply, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=6, column=2, sticky=E)

        Label(window, text="Total Divide:", font="Helvetica 16").grid(
            row=7, column=1, sticky=W)
        Label(window, textvariable=self.total_divide, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=7, column=2, sticky=E)

        Button(window, text="Calculate", command=self.calc,
               font="Helvetica 14").grid(row=10, column=2, padx=(100, 5), pady=5)

        window.mainloop()

    def calc(self):
        number1 = int(self.number1.get())
        number2 = float(self.number2.get())

        total_add = number1 + number2
        total_subtract = number2 - number1
        total_multiply = number1 * number2

        if number1 is 0:
            total_divide = "Error"
            self.total_divide.set(format(total_divide))
        else:
            total_divide = number2 / number1
            self.total_divide.set(format(total_divide, "5,.2f"))

        self.total_add.set(format(total_add, "5,.2f"))
        self.total_subtract.set(format(total_subtract, "5,.2f"))
        self.total_multiply.set(format(total_multiply, "5,.2f"))


Calculations()
