import tkinter as tk
from tkinter import *
import threading
import winsound
from fontTools.ttLib import TTFont

font = TTFont("C:/Users/lugz2/PycharmProjects/StarWarsGUIChanger/Starjedi.ttf")

window = Tk()
window.config(bg="black")
starwars = tk.Label(
    text="A long time ago in a galaxy far far away...",
    fg="lightBlue",
    bg="black",
    height=800,
    width=400,
    font=(None, 20)
)
window.title("Star Wars")
window.geometry("800x400")
starwars.pack()


def play():
    winsound.PlaySound("swtheme.wav", winsound.SND_ALIAS)


def newwindow():
    window2 = Tk()
    window2.config(bg="black")
    starwarsnew = tk.Label(
        window2,
        text="STAR WARS",
        fg="yellow",
        bg="black",
        height=800,
        width=400,
        font=("Star Jedi", 80)
    )
    window2.title("STAR WARS")
    window2.geometry("800x400")
    starwarsnew.pack()


def printtext():
    threadsound.start()
    print("STAR WARS")
    newwindow()


threadsound = threading.Thread(target=play)

button = Button(window, text="PLAY", fg="lightBlue", bg="black", width=10, command=printtext).place(x=350, y=300)

starwars.mainloop()
