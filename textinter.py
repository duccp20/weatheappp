
from tkinter import *
root = Tk()

global entry
global colour


def callback(*args):
    for i in range(len(colour)):
        if entry.get().lower() == test[i].lower():
            entry.configure({"background": colour[i]})
            break
        else:
            entry.configure({"background": "white"})


var = StringVar()
entry = Entry(root, textvariable=var)
test = ["Yes", "No", "Maybe"]
colour = ["Red", "Green", "Blue"]
var.trace(mode="w", callback=callback)

entry.pack()
root.mainloop()
