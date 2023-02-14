from tkinter import *
from tkinter import ttk


def calc():
    op1 = float(operand1text.get())
    op2 = float(operand2text.get())
    oper = operationtext.get()
    
    if oper == "+":
        result = op1 + op2
    elif oper == "-":
        result = op1 - op2
    elif oper == "/":
        result = op1 / op2
    elif oper == "*":
        result = op1 * op2
    
    resultTxt = str(result)
    outputLbl.config(text=resultTxt)


window = Tk()

window.geometry("400x300")
window.title("Simple Calculator")

operand1text = StringVar()
operand2text = StringVar()
operationtext = StringVar()


calcBtn = Button(window, text="Calculate", font=("Helvetica", 14), command=calc)
input1Ent = Entry(window,font=("Helvetica", 14), textvariable=operand1text)
input2Ent = Entry(window,font=("Helvetica", 14), textvariable=operand2text)
outputLbl = Label(window, text="0", font=("Helvetica", 14))
comboCmb = ttk.Combobox(window, width=10, font=("Helvetica", 14), textvariable=operationtext)

comboCmb['values'] = ('+', '-', '*', '/')

comboCmb.current(0)

calcBtn.place(x='170', y='100')
comboCmb.place(x='10', y='100')
input1Ent.place(x='10', y='10')
input2Ent.place(x='180', y='10')
outputLbl.place(x='150', y='200')

window.mainloop()
