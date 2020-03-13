from tkinter import *

window = Tk()
window.title("Reinforcement Learning Experiments with the Boardgame Lords of Waterdeep")
window.configure(background="black")
lbl = Label(window, text="Welcome to this experiment")
lbl.grid(column=0, row=0)

def getPlayerInputChoice(choices):
    return 0

def setDiplayText(displaytext):
    lbl.configure(text=displaytext)

window.mainloop()