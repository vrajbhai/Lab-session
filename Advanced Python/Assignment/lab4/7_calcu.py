from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x300")

e1 = Entry(window)
e1.pack()

e2 = Entry(window)
e2.pack()

result = Label(window, text="Answer")
result.pack()


def add():
    ans = int(e1.get()) + int(e2.get())
    result.config(text="Answer = " + str(ans))


def sub():
    ans = int(e1.get()) - int(e2.get())
    result.config(text="Answer = " + str(ans))


def mul():
    ans = int(e1.get()) * int(e2.get())
    result.config(text="Answer = " + str(ans))


def div():
    ans = int(e1.get()) / int(e2.get())
    result.config(text="Answer = " + str(ans))


Button(window, text="Add", command=add).pack()
Button(window, text="Subtract", command=sub).pack()
Button(window, text="Multiply", command=mul).pack()
Button(window, text="Divide", command=div).pack()

window.mainloop()