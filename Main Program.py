import tkinter as tk
from PIL import ImageTk,Image
import random

def tail_():
    global result

    h_t = tk.Tk()

    h_t.geometry("250x250")

    h_t.title("WIN OR LOSS")

    h_t.maxsize(250,250)

    h_t.minsize(250,250)

    result = random.randint(a = 0, b = 1)

    if result == 0:
        label_1 = tk.Label(master=h_t, text = "You win its a Tail",font = ("Courier", 10))

        label_1.place(x = 40, y = 10)
    else:
        label_2 = tk.Label(master=h_t, text = "You Loss its a Head",font = ("Courier", 10))

        label_2.place(x = 40, y = 10)

    h_t.mainloop()

def head_():
    global result

    h_t = tk.Tk()

    h_t.geometry("250x100")

    h_t.title("WIN OR LOSS")

    h_t.maxsize(250,100)

    h_t.minsize(250,100)

    result = random.randint(a = 0, b = 1)

    if result == 0:
        label_1 = tk.Label(master=h_t, text = "You win its a Head",font = ("Courier", 10))


        label_1.place(x = 40, y = 10)
    else:
        label_2 = tk.Label(master=h_t, text = "You Loss its a Tail",font = ("Courier", 10))

        label_2.place(x = 40, y = 10)

    h_t.mainloop()

def toss():

    Tk_instance.destroy()
    
    window = tk.Tk()

    window.geometry("1320x720")

    window.title("Toss")

    window.minsize(1320,720)

    Text_label = tk.Label(master=window, text = "Choose Head or Tail",font = ("Courier", 30))

    Text_label.place(x = 445, y = 250)

    head_button = tk.Button(master=window, text = "Head",width = 30, height =  3,font = ("Courier", 10),command = head_)

    head_button.place(x = 330, y = 370)

    tail_button  = tk.Button(master=window, text = "Tail", width = 30, height = 3,font = ("Courier", 10),command = tail_)

    tail_button.place(x  = 750 , y = 370)

    window.mainloop()

def match():
    Tk_instance.destroy()

    M_t = tk.Tk()

    M_t.title("Teams")

    M_t.minsize(1320,720)

    M_t.geometry("1320x720")

    


Tk_instance = tk.Tk()

Tk_instance.title("Cricket Board(True Score)")

Tk_instance.minsize(1320,720)

Tk_instance.geometry("1320x720")

toss_button = tk.Button(master= Tk_instance, text = "Toss", width = 30, height = 3, command = toss,font = ("Courier", 10))

toss_button.place(x = 330, y = 370)

match_button = tk.Button(master= Tk_instance, text = "Match", width = 30, height = 3,font = ("Courier", 10),command = match)

match_button.place(x = 750, y = 370)

Tk_instance.mainloop()