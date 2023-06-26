import pymysql
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import messagebox as msg
import random
from threading import Thread
from time import sleep

is_game_started = False
cleaned_houses = 0
bombs = []
NUMBER_OF_BOMBS = 5
WIDTH = 5
HEIGHT = 5
h=0
m=0
s=0

if NUMBER_OF_BOMBS >= WIDTH*HEIGHT:
    msg.showerror("Error", "Not enough space for bombs!!!")
    exit()

def count_time():
    global h, m, s
    while is_game_started:
        sleep(1)
        s += 1
        if s == 60:
            s=0
            m+=1
            if m==60:
                m=0
                h+=1
        ime['text']=f"{h:02}:{m:02}:{s:02}"

def right_click(event):
    t = event.widget['text']
    if t == 'flag':
        event.widget.configure(text="")
    elif t == "":
        event.widget.configure(text="flag")

def create_bombs(i, j):
    counter = 0
    while counter < NUMBER_OF_BOMBS:
        random_i = random.randint(0, HEIGHT-1)
        random_j = random.randint(0, WIDTH-1)
        new_bomb = (random_i, random_j)
        if (new_bomb not in bombs) and (new_bomb != (i, j)):
            bombs.append(new_bomb)
            counter+=1
    print(bombs)

def save_records():
    msg.askquestion("End", "Want to Save your record?")
    # todo with database

def check_itself(i, j):
    global cleaned_houses, is_game_started
    number_of_bombs_around = 0
    if houses[i][j]['text']=="flag":
        ans = msg.askquestion("Warning", "This house is a flag!!!\nAre you sure you want to click it?")
        if ans == "no":
            return
        else:
            houses[i][j]['text']=""
    if (i, j) in bombs:
        print("Boom!")
        is_game_started=False
        save_records()
        exit()
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            try:
                if (k, l) in bombs:
                    number_of_bombs_around+=1
            except:
                pass
    if number_of_bombs_around > 0:
        houses[i][j].config(state="disabled", text=number_of_bombs_around)
        cleaned_houses += 1
    elif number_of_bombs_around == 0:
        houses[i][j].config(state="disabled")
        cleaned_houses += 1
    if cleaned_houses == WIDTH*HEIGHT-NUMBER_OF_BOMBS:
        is_game_started=False
        msg.showinfo("Winner", "You have found all the bombs.")
        save_records()
        exit()

def find_all_numbers():
    for i in range(0, WIDTH):
        houses_numbers.append([])
        for j in range(0, HEIGHT):
            number = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    try:
                        if (k, l) in bombs and (k, l) != (i, j):
                            number+=1
                    except:
                        pass
            houses_numbers[i].append(number)
    for m in houses_numbers:
        print(m)
                
                

def check_around(i, j):
    pass

def click(i, j):
    global is_game_started
    if is_game_started==False:
        create_bombs(i, j)
        find_all_numbers()
        is_game_started=True
        Thread(target=count_time, daemon=True).start()

    check_itself(i, j)
    check_around(i, j)
    # print(i, j)

houses = []
houses_numbers = []
root=tk.Tk()
frm=tk.Frame(root).grid(row=1,column=1,sticky="news")
ime=tk.Label(frm,text=f"{h:02}:{m:02}:{s:02}",font=("ds-digital",25),bg="black",fg="red")
if WIDTH % 2 == 0:
    ime.grid(row=0,column=WIDTH//2-1,columnspan=4,sticky="news")
elif WIDTH % 2 == 1:
    ime.grid(row=0,column=WIDTH//2,columnspan=3,sticky="news")
for i in range(HEIGHT):
    houses.append([])
    for j in range(WIDTH):
        houses[i].append(tk.Button(root, width=10, height=5, command=lambda i=i, j=j: click(i, j)))
        houses[i][j].bind("<Button-3>", right_click)
        houses[i][j].grid(row=i+1,column=j+1)

root.mainloop()
