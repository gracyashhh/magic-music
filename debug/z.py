import threading
from tkinter import *
from tkinter.ttk import *
window = Tk()
e = Entry(window, width=100)
e.pack()
player2 = ""

def get_text():
    e.config(state='disabled')
    global player2
    player2 = e.get()
    return player2

Button(window, text="done", command=get_text).pack()

def logic():
    global player2
    Label(window, text="Times up").pack()
    e.config(state='disabled')
    player2 = e.get()
threading.Timer(60.0, logic).start()

Label(window, text=player2).pack()
window.mainloop()