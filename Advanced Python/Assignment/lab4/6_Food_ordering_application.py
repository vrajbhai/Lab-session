from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Food Order")
window.geometry("300x250")

pizza = IntVar()
burgur = IntVar()
coke = IntVar()

Checkbutton(window, text="Pizza (200)", variable=pizza).pack()
Checkbutton(window, text="Burgur (100)", variable=burgur).pack()
Checkbutton(window, text="Coke (50)", variable=coke).pack()

def bill():
    total = 0

    if pizza.get():
        total += 200

    if burger.get():
        total += 100

    if coke.get():
        total += 50

    messagebox.showinfo("Bill", "Total Bill = ₹" + str(total))


Button(window, text="Place Order", command=bill).pack(pady=20)

window.mainloop()