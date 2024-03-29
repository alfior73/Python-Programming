from tkinter import *
import numpy_financial as npf


class RefiEval:

    def __init__(self):
        window = Tk()
        window.title("Refinance Evaluator")

        Label(window, text="Loan Amount", font="Helvetica 16").grid(
            row=1, column=1, sticky=W)
        Label(window, text="Interest Rate", font="Helvetica 16").grid(
            row=2, column=1, sticky=W)
        Label(window, text="Term (years)", font="Helvetica 16").grid(
            row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1, sticky=W)

        Label(window, text="Payment:", font="Helvetica 16").grid(
            row=5, column=1, sticky=W)
        Label(window, text="Total Payments:", font="Helvetica 16").grid(
            row=6, column=1, sticky=W)

        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

        self.pmt = StringVar()
        self.total = StringVar()

        Entry(window, textvariable=self.pv, justify=RIGHT).grid(
            row=1, column=2, padx=(0, 5))
        Entry(window, textvariable=self.interest_rate, justify=RIGHT).grid(
            row=2, column=2, padx=(0, 5))
        Entry(window, textvariable=self.term, justify=RIGHT).grid(
            row=3, column=2, padx=(0, 5))

        Label(window, textvariable=self.pmt, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2, sticky=E)
        Label(window, textvariable=self.total, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=6, column=2, sticky=E)

        Button(window, text="Calculate Payment", command=self.calcPayment,
               font="Helvetica 14").grid(row=7, column=2, padx=(100, 5), pady=5)

        window.mainloop()

    def calcPayment(self):
        pv = float(self.pv.get())
        rate = float(self.interest_rate.get())
        term = int(self.term.get())

        pmt = npf.pmt(rate /1200, term * 12, -pv, 0)
        total = pmt * 12 * term

        self.pmt.set("$"+format(pmt, "5,.2f"))
        self.total.set("$"+format(total, "8,.2f"))


RefiEval()
